import allure
import json
from allure_commons.types import AttachmentType


class Helper:
    # метод берет response, делает из него json и прикрепляет этот json к allure-отчёту
    def attach_response(self, response):
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name='API Response', attachment_type=AttachmentType.JSON)
        