import dataclasses


@dataclasses.dataclass
class ServiceBaseRequest:
    service: str = 'pcb'
    region_id: str = '211'  # TODO
    country: str = '211'  # TODO
    express: str = '31'  # TODO
