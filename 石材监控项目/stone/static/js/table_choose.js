cityareaname=new Array(35);
cityareacode=new Array(35);
 function first(preP,preC,formname,selectP,selectC)
   {
     a=0;
if (selectP=='01')
  { a=1;tempoption=new Option('1#排锯','pg0001',false,true); }
else
  { tempoption=new Option('1#排锯','pg0001'); }
eval('document.'+formname+'.'+preP+'.options[1]=tempoption;');
       cityareacode[0]=new Array('currentflow','mompower','fwrotspeed','fwcurrflow','cutspeed','cutratio','totalpower');
       cityareaname[0]=new Array('瞬时电流','瞬时总功率','飞轮转速','飞轮电流','切割速度','切割效率','总用电量');
if (selectP=='02')
  { a=2;tempoption=new Option('1#磨机','mj0001',false,true); }
else
  { tempoption=new Option('1#磨机','mj0001'); }
eval('document.'+formname+'.'+preP+'.options[2]=tempoption;');
cityareacode[1]=new Array('currentflow','mompower','beltspeed','beamswingspeed','grindratio','totalpower');
cityareaname[1]=new Array('瞬时电流','瞬时总功率','皮带速度','横梁摆动速度','磨抛效率','总用电量');
if (selectP=='03')
  { a=3;tempoption=new Option('1#补胶线A箱','bjx0001a',false,true); }
else
  { tempoption=new Option('1#补胶线A箱','bjx0001a'); }
eval('document.'+formname+'.'+preP+'.options[3]=tempoption;');
cityareacode[2]=new Array('momcurrenta','mompowera','tempea','humiditya','powera');
cityareaname[2]=new Array('A箱电流','A箱功率','A箱温度','A箱湿度','A箱用电量');
if (selectP=='04')
  { a=4;tempoption=new Option('1#补胶线B箱','bjx0001b',false,true); }
else
  { tempoption=new Option('1#补胶线B箱','bjx0001b'); }
eval('document.'+formname+'.'+preP+'.options[4]=tempoption;');
       cityareacode[3]=new Array('momcurrentb','mompowerb','tempeb','humidityb','powerb','totalpower','mompower','tacttiming');
       cityareaname[3]=new Array('B箱电流','B箱功率','B箱温度','B箱湿度','B箱用电量','总用电量','瞬时总功率','生产节拍');

eval('document.'+formname+'.'+preP+'.options[a].selected=true;');
cityid=selectP;
    if (cityid!='0')
      {
        b=0;for (i=0;i<cityareaname[cityid-1].length;i++)
           {
             if (selectC==cityareacode[cityid-1][i])
               {b=i+1;tempoption=new Option(cityareaname[cityid-1][i],cityareacode[cityid-1][i],false,true);}
             else
               tempoption=new Option(cityareaname[cityid-1][i],cityareacode[cityid-1][i]);
            eval('document.'+formname+'.'+preC+'.options[i+1]=tempoption;');
           }
        eval('document.'+formname+'.'+preC+'.options[b].selected=true;');
      }
    }
 function selectcityarea(preP,preC,formname)
   {
     cityid=eval('document.'+formname+'.'+preP+'.selectedIndex;');
     j=eval('document.'+formname+'.'+preC+'.length;');
     for (i=1;i<j;i++)
        {eval('document.'+formname+'.'+preC+'.options[j-i]=null;')}
     if (cityid!="0")
       {
         for (i=0;i<cityareaname[cityid-1].length;i++)
            {
             tempoption=new Option(cityareaname[cityid-1][i],cityareacode[cityid-1][i]);
             eval('document.'+formname+'.'+preC+'.options[i+1]=tempoption;');
            }
       }
    }