n1 = float(input('Digite um valor em metros: '))
km = n1 * 0.001
hm = n1 * 0.01
dam = n1 * 0.1
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000
print('Esta medida de {}m vale: \n{}km\n{}hm\n{:.2f}dam\n{}dm\n{}cm\n{}mm'.format(n1, km, hm, dam, dm, cm, mm))
