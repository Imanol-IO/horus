from satcfdi.models import Signer
from satcfdi.portal import SATFacturaElectronica

# Load Fiel
signer = Signer.load(
    certificate=open('/home/imanol/Documentos/FIEL_IAOI9901221D8_20230804093145/00001000000701570635.cer', 'rb').read(),
    key=open('/home/imanol/Documentos/FIEL_IAOI9901221D8_20230804093145/Claveprivada_FIEL_IAOI9901221D8_20230804_093145.key', 'rb').read(),
    password='Sk4dy241'
)

sat_session = SATFacturaElectronica(signer)
sat_session.login()


# Validación RFC
res = sat_session.rfc_valid(
    rfc='IAOI9901221D8'
)
print(res)

# Validación Razón Social
res = sat_session.legal_name_valid(
    rfc='IAOI9901221D8',
    legal_name='KIJ, S.A DE C.V.'
)
print(res)

# LCO Detalles
res = sat_session.lco_details(rfc="IAOI9901221D8")
print(res)