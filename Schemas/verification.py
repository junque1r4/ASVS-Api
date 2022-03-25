def verificationEntity(item) -> dict:
    return {
        "chapter": item["chapter_id"],
        "requirement_id": item["req_id"],
        "cwe": item["cwe"],
        "NIST": item["nist"],
        "description": item["req_description"],
        "section_name": item["section_name"],
        "level1": item["level1"],
        "level2": item["level2"],
        "level3": item["level3"],
    }


def verificationEntitys(entity) -> list:
    return [verificationEntity(item) for item in entity]
