# Image to ASCII art 
 
In this repository presented are three algorithms for converting images to ASCII art.

`by_gradient.py`, it simply transposes the selected character gradient to the brightness of the image.

```
@@@0000###XXXOOOoooxx+++***'''...````   
@@@0000###XXXOOOoooxx+++***'''...````   
@@@0000###XXXOOOoooxx+++***'''...````   
@@@0000###XXXOOOoooxx+++***'''...````   
@@@0000###XXXXOoxxxxxxxx+*''''...````   
@@@0000###XXO+'''*+xxoOXXXo*''...````   
@@@0000####+``.''*+xxoOXX#00o....````   
@@@0000###x ``.''*+xxoOXX#00@x...````   
@@@0000###' ``.''*+xxoOXX#00@X...````   
@@@0000###x ``.''*+xxoOXX#00@x...````   
@@@0000###X+``.''*+xxoOXX#00o'...````   
@@@0000###XXo*'''*+xxoOXXXO+''...````   
@@@0000###XXXXOoxxxxxxxx+*''''...````   
@@@0000###XXXOOOoooxx+++***'''...````   
@@@0000###XXXOOOoooxx+++***'''...````   
@@@0000###XXXOOOoooxx+++***'''...````   
@@@0000###XXXOOOoooxx+++***'''...````   
```

---

`by_tone.py`, selects the most similar in tone symbol for the segment.

```
@@@@@QQQQQ&M08DOG4P]yCTs?r>!~,"::'-``  
@@@@@QQQQQ&M08DOG4P]yCTs?r>!~,"::'-``  
@@@@@QQQQQ&M08DOG4P]yCTs?r>!~,"::'-``  
@@@@@QQQQQ&M08DOG4P]yCTs?r>!~,"::'-``  
@@@@@QQQQQ&M08D4e[[I5EEeJr>!~,"::'-``  
@@@@@QQQQQ&MO|^,=c)[EVm#WgGL~,"::'-``  
@@@@@QQQQQ&J`':,=c)[EVm#WQQQk,"::'-``  
@@@@@QQQQQy `':,=c)[EVm#WQQ@@Z"::'-``  
@@@@@QQQQQ~ `':,=c)[Eqm#WQQ@@#"::'-``  
@@@@@QQQQQY `':,=c)[Eqm#WQQ@@j"::'-``  
@@@@@QQQQQ&)`':,=c)[EVm#WQQQ4,"::'-``  
@@@@@QQQQQ&MOv,,=c)[EVm#WWK?~,"::'-``  
@@@@@QQQQQ&M08XbZ11y52Shnr>!~,"::'-``  
@@@@@QQQQQ&M08DOG4P]yCTs?r>!~,"::'-``  
@@@@@QQQQQ&M08DOG4P]ICTs?r>!~,"::'-``  
@@@@@QQQQQ&M08DOG4P]yCTs?r>!~,"::'-``  
```

---

`by_similarity.py`, selects the most similar-shaped symbol for the segment.

```
@@@@@@@@@@@BBBBEEE|::`                 
@@@@@@@@@@@BBBBEEE|::`                 
@@@@@@@@@@@BBBBEEE|::`                 
@@@@@@@@@@@BBBBEEE|::`                 
@@@@@@@@@@@BBBBF^""`:\,,_              
@@@@@@@@@@@BB"     :\ZZBB@g_           
@@@@@@@@@@@F       :\ZZBB@@@g          
@@@@@@@@@@F        :\ZZBB@@@@L         
@@@@@@@@@@         :\ZZBB@@@@[         
@@@@@@@@@@L        :\ZZBB@@@@F         
@@@@@@@@@@@,       :\ZZBB@@@F          
@@@@@@@@@@@Bp,     :\ZZBBBP            
@@@@@@@@@@@BBBBbu..:!^^"               
@@@@@@@@@@@BBBBEEE|::`                 
@@@@@@@@@@@BBBBEEE|::`                 
@@@@@@@@@@@BBBBEEE|::`                 
```
