davhar, orts, hToo = map(int, input().split())
hDugaar = int(input())

# orts, davhar, heddeh haalga

if hDugaar % hToo == 0:
    print(hDugaar//hToo, hToo)
else:
    print(hDugaar//hToo+1, hDugaar % hToo)

# zaa davhar, heddeh haalgiin oltson
# ortsiig n olno
# orts davhar
if hDugaar//hToo % orts == 0:
    print()
