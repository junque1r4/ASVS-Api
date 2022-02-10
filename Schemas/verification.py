def verificationEntity(item) -> dict:
    return {
        "area": item["area"],
        "id": item["id"],
        "criticity": item["criticity"],
        "cwe": item["cwe"],
        "NIST": item["NIST"],
        "requisito": item["requisito"],
    }


def verificationEntitys(entity) -> list:
    return [verificationEntity(item) for item in entity]
