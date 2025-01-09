import re

import requests
from playwright.sync_api import Page


def get_url_parameters_as_dict(page: Page):
    current_url = page.url

    params = page.evaluate("""
    url => {
        let params = {};
        for (const [key, value] of new URL(url).searchParams.entries()) {
            params[key] = value;
        }
        return params;
    }
    """, current_url)

    return params


def get_area_from_response_for_mining_allotment(page: Page):
    params = get_url_parameters_as_dict(page)

    query_params = {
        "pid": params.get("pid"),
        "objectId": params.get("tapId"),
        "spatialReferenceId": "null",
        "isDms": "false"
    }
    s_cookies = {
        "Web2Sl_Prj_0262bc35-8519-4fe2-00d6-75f081bc55e3": "d5eny1afrdqy00"
    }

    # URL для запроса, нужно будет убрать куда нибудь в конфиги
    url = "https://redos-smn.sgp2.local/gp-dev-smn/api/LicensingUran/GetMountainTapGeometry"

    try:
        response = requests.get(url, params=query_params,
                                cookies=s_cookies, verify=False)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Ошибка при выполнении API-запроса:", e)
        return None


def get_area_from_response_for_licensed_area(page: Page):
    params = get_url_parameters_as_dict(page)
    # код чтобы получить значение part_id, млишком сложный, может быть стоит просто захардкодить
    tree_path = params.get("treePath", "")
    part_id = re.search(r"([0-9a-fA-F-]+)$", tree_path).group(1) if tree_path else None

    query_params = {
        "pid": params.get("pid"),
        "partId": part_id,
        "spatialReferenceId": "null",
        "isDms": "true"
    }
    s_cookies = {
        "Web2Sl_Prj_0262bc35-8519-4fe2-00d6-75f081bc55e3": "d5eny1afrdqy00"
    }

    # URL для запроса, нужно будет убрать куда нибудь в конфиги
    url = "https://redos-smn.sgp2.local/gp-dev-smn/api/LicensingUran/GetGeometry"

    try:
        response = requests.get(url, params=query_params,
                                cookies=s_cookies, verify=False)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Ошибка при выполнении API-запроса:", e)
        return None


def get_contour_area(page: Page, response_func="mining"):
    if response_func == "licensed":
        response_data = get_area_from_response_for_licensed_area(page)
    else:
        response_data = get_area_from_response_for_mining_allotment(page)
    area = response_data.get("area")
    if area is not None:
        area = round(area, 2)

    return area
