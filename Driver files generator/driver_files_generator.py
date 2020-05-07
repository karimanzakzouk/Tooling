import os 
import shutil

os.mkdir('cots')
print("enter layer name :")
layer_name= input()

print("enter driver name :")
driver_name= input()

os.chdir('./cots')
os.mkdir(layer_name)
os.chdir('./'+str(layer_name)) 
os.mkdir(driver_name)
os.chdir('./'+str(driver_name))

f1=open(str(driver_name+'_int.h'),'w')
f2=open(str(driver_name+'_reg.h'),'w')
f3=open(str(driver_name+'_priv.h'),'w')
f4=open(str(driver_name+'_cfg.h'),'w')
f5=open(str(driver_name+'_prog.c'),'w')

f1.write('#ifndef '+str(layer_name.upper())+'_'+str(driver_name.upper())+'_INT_H_\n'+
'#define '+str(layer_name.upper())+'_'+str(driver_name.upper())+'_INT_H_\n'+ 
'#include \"'+'STD_TYPES.h\"'+'\n\n'+'\n\n\n#endif ')

f2.write('#ifndef '+str(layer_name.upper())+'_'+str(driver_name.upper())+'_REG_H_\n'+
'#define '+str(layer_name.upper())+'_'+str(driver_name.upper())+
'_REG_H_\n\n\n\n'+'#endif ')

f3.write('#ifndef '+str(layer_name.upper())+'_'+str(driver_name.upper())+'_PRIV_H_\n'+
'#define '+str(layer_name.upper())+'_'+
str(driver_name.upper())+'_PRIV_H_\n\n\n' +'#endif')

f4.write('#ifndef '+str(layer_name.upper())+'_'+str(driver_name.upper())+'_CFG_H_\n'+
'#define '+str(layer_name.upper())+'_'+
str(driver_name.upper())+'_CFG_H_\n\n\n' +'#endif')

f5.write('#include \"'+'STD_TYPES.h\"'+
'\n#include \"'+'MACROS.h\"'+
'\n#include \"'+driver_name+'_int.h\"'+
'\n#include \"'+driver_name+'_priv.h\"'+
'\n#include \"'+driver_name+'_cfg.h\"'+
'\n#include \"'+driver_name+'_reg.h\"')

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

