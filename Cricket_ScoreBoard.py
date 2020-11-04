from tkinter import *
import csv
from pandas import *
from matplotlib import pyplot as plt

score1=0 #Main Score
score2=0 #B1 Score
score3=0 #B2 Score
ballsplayed=0 #B1 Played
ballsplayed2=0 #B2 Played
wickets=0 #Wickets
balls1=0 #Main Balls
overs=0 #No of overs till now(1.2)
a=0
Strike_List=['Batsman-1 Name','Batsman-2 Name'] #To store the Name of the Batsman currently playing
Strike_Pointer=0 #To know who is on the ONSIDE
auto_checker=0 #To check whether to do work automatically or not
evod=1 #To maipulate the value of "auto_checker"
out_reason="" #Why the player is OUT
out_reason_checker=0 #To check whether end user has provided the reason or not
Clear_Out_Reason="Out Reason" #A Pre-placed value
CSV_checker=0 #To check a new CSV file is created or the existing file overwritten or not

class Destination:
        def __init__(self,root):
                self.root=root
                self.root.title("Online Score Board")
                self.root.geometry("1270x200+0+0") 
                root.iconbitmap(r'ball.ico')                     #fevicon icon

        #===========Frame-1================
                frame1=Frame(self.root,bg='#2c2c2c')
                frame1.place(x=300,y=50,width=750,height=50)

        #===========Team Label================
                self.t_name=StringVar()
                self.t_name.set("TEAM")
                self.teamlb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.t_name,font=("",15,"bold"))
                self.teamlb1.pack(side=LEFT)

        #===========score Label================
                self.scr=StringVar()
                self.scr.set("0")
                self.scoreb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.scr,font=("",15,"bold"))
                self.scoreb1.pack(side=LEFT,padx=(10,0))
        #===========Wicket Label================
                self.wkt=StringVar()
                self.wkt.set("- 0")
                self.wktlb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.wkt,font=("",15,"bold"))
                self.wktlb1.pack(side=LEFT)

        #===========Over-after -6 -balls Label================
                self.ovr=StringVar()
                self.ovr.set("0")
                self.ovrlb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.ovr,font=("",15,"bold"))
                self.ovrlb1.pack(side=LEFT,padx=(10,0))

        #===========Balls- Label================
                self.balls=StringVar()
                self.balls.set(".0")
                self.balllb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.balls,font=("",15,"bold"))
                self.balllb1.pack(side=LEFT)


        #===========Total overs Label================
                self.over=StringVar()
                self.over.set("/ 0")
                self.overlb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.over,font=("",15,"bold"))
                self.overlb1.pack(side=LEFT)


        #===========BATSMAN-1 Label================
                self.strike1=StringVar()
                self.strike1.set("")
                self.strike1lb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.strike1,font=("",25,"bold"))
                self.strike1lb1.pack(side=LEFT,padx=(15,0))

                self.B1=StringVar()
                self.B1.set("Batsman-1 Name")
                self.B1lb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.B1,font=("",15,"bold"))
                self.B1lb1.pack(side=LEFT,padx=(2,0))

                self.B1scr=StringVar()
                self.B1scr.set("0")
                self.B1scrlb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.B1scr,font=("",15,"bold"))
                self.B1scrlb1.pack(side=LEFT,padx=(5,0))

                self.B1ball=StringVar()
                self.B1ball.set("(0)")
                self.B1balllb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.B1ball,font=("",15,"bold"))
                self.B1balllb1.pack(side=LEFT)


        #===========BATSMAN-2 Label================
                self.strike2=StringVar()
                self.strike2.set("")
                self.strike2lb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.strike2,font=("",25,"bold"))
                self.strike2lb1.pack(side=LEFT,padx=(5,0))

                self.B2=StringVar()
                self.B2.set("Batsman-2 Name")
                self.B2lb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.B2,font=("",15,"bold"))
                self.B2lb1.pack(side=LEFT,padx=(2,0))

                self.B2scr=StringVar()
                self.B2scr.set("0")
                self.B2scrlb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.B2scr,font=("",15,"bold"))
                self.B2scrlb1.pack(side=LEFT,padx=(5,0))

                self.B2ball=StringVar()
                self.B2ball.set("(0)")
                self.B2balllb1=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.B2ball,font=("",15,"bold"))
                self.B2balllb1.pack(side=LEFT)



#Functions


#===========Strike changer function=============

        def strike(self):
                global Strike_Pointer
                Strike_Pointer=0
                self.strike1.set("*")
                self.strike2.set("")

        def strik(self):
                global Strike_Pointer
                Strike_Pointer=1
                self.strike2.set("*")
                self.strike1.set("")


        #===========Score update===========

        def scr1(self):
                global score1,auto_checker,Strike_Pointer
                score1+=1
                self.scr.set(score1)
                if auto_checker==1:
                        if Strike_Pointer==0:
                                global score2
                                score2+=1
                                self.B1scr.set(score2)
                                self.strike1.set("*")
                                self.strike2.set("")
                                Strike_Pointer=1
                        else:
                                global score3
                                score3+=1
                                self.B2scr.set(score3)
                                self.strike2.set("*")
                                self.strike1.set("")
                                Strike_Pointer=0
                else:
                        pass
        
        def scr2(self):
                global score1,auto_checker,Strike_Pointer
                score1+=2
                self.scr.set(score1)
                if auto_checker==1:
                        if Strike_Pointer==0:
                                global score2
                                score2+=2
                                self.B1scr.set(score2)
                                self.strike1.set("*")
                                self.strike2.set("")
                        else:
                                global score3
                                score3+=2
                                self.B2scr.set(score3)
                                self.strike2.set("*")
                                self.strike1.set("")
                else:
                        pass

        def scr3(self):
                global score1,auto_checker,Strike_Pointer
                score1+=3
                self.scr.set(score1)
                if auto_checker==1:
                        if Strike_Pointer==0:
                                global score2
                                score2+=3
                                self.B1scr.set(score2)
                                self.strike1.set("*")
                                self.strike2.set("")
                                Strike_Pointer=1
                        else:
                                global score3
                                score3+=3
                                self.B2scr.set(score3)
                                self.strike2.set("*")
                                self.strike1.set("")
                                Strike_Pointer=0
                else:
                        pass 

        def scr4(self):
                global score1,auto_checker,Strike_Pointer
                score1+=4
                self.scr.set(score1)
                if auto_checker==1:
                        if Strike_Pointer==0:
                                global score2
                                score2+=4
                                self.B1scr.set(score2)
                                self.strike1.set("*")
                                self.strike2.set("")
                        else:
                                global score3
                                score3+=4
                                self.B2scr.set(score3)
                                self.strike2.set("*")
                                self.strike1.set("")
                else:
                        pass

        def scr5(self):
                global score1,auto_checker,Strike_Pointer
                score1+=5
                self.scr.set(score1)
                if auto_checker==1:
                        if Strike_Pointer==0:
                                global score2
                                score2+=5
                                self.B1scr.set(score2)
                                self.strike1.set("*")
                                self.strike2.set("")
                                Strike_Pointer=1
                        else:
                                global score3
                                score3+=5
                                self.B2scr.set(score3)
                                self.strike2.set("*")
                                self.strike1.set("")
                                Strike_Pointer=0
                else:
                        pass 

        def scr6(self):
                global score1,auto_checker,Strike_Pointer
                score1+=6
                self.scr.set(score1)
                if auto_checker==1:
                        if Strike_Pointer==0:
                                global score2
                                score2+=6
                                self.B1scr.set(score2)
                                self.strike1.set("*")
                                self.strike2.set("")
                        else:
                                global score3
                                score3+=6
                                self.B2scr.set(score3)
                                self.strike2.set("*")
                                self.strike1.set("")
                else:
                        pass

        def scrminus(self):
                global score1,auto_checker,Strike_Pointer
                score1-=1
                if (score1>=0):
                        self.scr.set(score1) 
                else:
                        score1=0
                        self.scr.set(score1)
                if auto_checker==1:
                        if Strike_Pointer==0:
                                global score2
                                score2-=1
                                if (score2>=0):
                                        self.B1scr.set(score2)
                                else:
                                        score2=0
                                        self.B1scr.set(score2)
                                self.strike1.set("*")
                                self.strike2.set("")
                        else:
                                global score3
                                score3-=1
                                if (score3>=0):
                                        self.B2scr.set(score3)
                                else:
                                        score3=0
                                        self.B2scr.set(score3)
                                self.strike2.set("*")
                                self.strike1.set("")
                else:
                        pass
        #===============Wicket update===============

        def wicket(self):
                global wickets,out_reason_checker,Clear_Out_Reason,Strike_List,Strike_Pointer,score2,score3,ballsplayed,ballsplayed2
                if out_reason_checker==1:
                        if (wickets<10):
                                wickets+=1
                                self.wkt.set("- "+str(wickets))
                                out_reason_checker=0
                                DC.Excel()
                                if(Strike_Pointer==0):
                                        self.B1.set("Batsman-1 Name")
                                        self.B1scr.set(0)
                                        self.B1ball.set("("+ str(0) +")")
                                        score2=0
                                        ballsplayed=0
                                else:
                                        self.B2.set("Batsman-2 Name")
                                        self.B2scr.set(0)
                                        self.B2ball.set("("+ str(0) +")")
                                        score3=0
                                        ballsplayed2=0



        def wicketminus(self):
                global wickets
                if (wickets>0):
                        wickets-=1
                        self.wkt.set("- "+str(wickets))

        
#===================over update===============

        def over_update(self):
                global a
                a=app1.t_overentry.get()
                if (len(a)!=0):
                        self.over.set("/ "+a)
                        app1.t_overentry.delete(0,'end')
                else:
                        self.over.set("/ 0")



        #===============Batsman -1 score update============

        def B1score1(self):
                global score2
                score2+=1
                self.B1scr.set(score2)
        def B1score2(self):
                global score2
                score2+=2
                self.B1scr.set(score2)
        def B1score3(self):
                global score2
                score2+=3
                self.B1scr.set(score2)
        def B1score4(self):
                global score2
                score2+=4
                self.B1scr.set(score2)
        def B1score5(self):
                global score2
                score2+=5
                self.B1scr.set(score2)
        def B1score6(self):
                global score2
                score2+=6
                self.B1scr.set(score2)
        def B1scoreminus(self):
                global score2
                score2-=1
                if (score2>=0):
                        self.B1scr.set(score2)
                else:
                        score2=0
                        self.B1scr.set(score2)

        #=============Batsman-1 Ball playes update==============

        def B1ballplay(self):
                global ballsplayed
                ballsplayed+=1
                self.B1ball.set("("+ str(ballsplayed) +")")

        def B1ballplayminus(self):
                global ballsplayed
                ballsplayed-=1
                if (ballsplayed<0):
                        ballsplayed=0
                        self.B1ball.set("("+str(ballsplayed)+")")
                else:
                        self.B1ball.set("("+str(ballsplayed)+")")

        #==============Batsman-1 name update==================

        def B1name_update(self):
                a=app1.B1name_entry.get()
                global Strike_List
                Strike_List[0]=a
                if (len(a)!=0):
                        self.B1.set(a.title())
                        app1.B1name_entry.delete(0,'end')
                else:
                        self.B1.set("Batsman-1 Name")

                
                


        #===============Batsman -2 score update============

        def B2score1(self):
                global score3
                score3+=1
                self.B2scr.set(score3)
        def B2score2(self):
                global score3
                score3+=2
                self.B2scr.set(score3)
        def B2score3(self):
                global score3
                score3+=3
                self.B2scr.set(score3)
        def B2score4(self):
                global score3
                score3+=4
                self.B2scr.set(score3)
        def B2score5(self):
                global score3
                score3+=5
                self.B2scr.set(score3)
        def B2score6(self):
                global score3
                score3+=6
                self.B2scr.set(score3)
        def B2scoreminus(self):
                global score3
                score3-=1
                if (score3>=0):
                        self.B2scr.set(score3)
                else:
                        score3=0
                        self.B2scr.set(score3)

        #=============Batsman-2 Ball played update==============

        def B2ballplay(self):
                global ballsplayed2
                ballsplayed2+=1
                self.B2ball.set("("+ str(ballsplayed2) +")")

        def B2ballplayminus(self):
                global ballsplayed2
                ballsplayed2-=1
                if (ballsplayed2<0):
                        ballsplayed2=0
                        self.B2ball.set("("+str(ballsplayed2)+")")
                else:
                        self.B2ball.set("("+str(ballsplayed2)+")")

        #==============Batsman-2 name update==================

        def B2name_update(self):
                a=app1.B2name_entry.get() 
                global Strike_List
                Strike_List[1]=a
                if (len(a)!=0):
                        self.B2.set(a.title())
                        app1.B2name_entry.delete(0,'end')
                else:
                        self.B2.set("Batsman-2 Name")

        #================Team name update==================
        def teamname_update(self):
                a=app1.teamname_entry.get()
                if (len(a)!=0):
                        self.t_name.set(a.upper())
                        app1.teamname_entry.delete(0,'end')
                else:
                        self.t_name.set("TEAM")

        #==============Team over update=====================
        def t_balls(self):
                global balls1,overs,a,auto_checker,Strike_Pointer
                check=float(f"{overs}.{balls1}")
                if(check==float(a)): #Return when exceed the number of overs
                        DC.End_Excel()
                        return 0
                balls1+=1
                self.balls.set("."+str(balls1))
                if (balls1>5):
                        self.balls.set(".0")
                        balls1=0
                        overs+=1
                        self.ovr.set(overs)
                
                if(auto_checker==1):
                        if(Strike_Pointer==0):
                                global ballsplayed
                                ballsplayed+=1
                                self.B1ball.set("("+ str(ballsplayed) +")")
                        else:
                                global ballsplayed2
                                ballsplayed2+=1
                                self.B2ball.set("("+ str(ballsplayed2) +")")
                else:
                        pass
                

        def t_ballsminus(self):
                global balls1,overs
                balls1-=1
                self.balls.set("."+str(balls1))
                if (balls1==-1 and overs>0 ):
                        balls1=5
                        self.balls.set("."+str(balls1))
                        overs-=1
                        self.ovr.set(overs)
                elif (overs==0 and balls1<0 and balls1<=1):
                        balls1=0
                        self.balls.set("."+str(balls1))
                if(auto_checker==1):
                        if(Strike_Pointer==0):
                                global ballsplayed
                                ballsplayed-=1
                                self.B1ball.set("("+ str(ballsplayed) +")")
                        else:
                                global ballsplayed2
                                ballsplayed2-=1
                                self.B2ball.set("("+ str(ballsplayed2) +")")
                else:
                        pass


        def Clear(self):
                global balls,overs,score1,score2,score3,balls1,ballsplayed,ballsplayed2,wickets,a,Strike_Pointer,evod,Clear_Out_Reason,out_reason_checker,CSV_checker
                self.balls.set('.0')
                self.B1ball.set('(0)')
                self.B2ball.set('(0)')
                score1=0
                score2=0
                score3=0
                balls1=0
                ballsplayed=0
                ballsplayed2=0
                balls=0
                wickets=0
                overs=0
                a=0
                Strike_Pointer=0
                evod=1
                out_reason_checker=0
                CSV_checker=0
                self.t_name.set("TEAM")
                self.wkt.set("- 0")
                self.B1scr.set('0')
                self.B2scr.set('0')
                self.B1.set("Batsman-1 Name")
                self.B2.set("Batsman-2 Name")
                self.ovr.set("0")
                self.scr.set("0")
                self.strike2.set("")
                self.strike1.set("")
                self.over.set("/ 0")
                


class Datastation:
        def __init__(self,root1):
                self.root1=root1
                self.root1.title("Data-Station")
                self.root1.geometry("1270x500+0+0")
                root1.iconbitmap(r'bat.ico')          #fevicon icon

        #=============Menu Bars============
                m=Menu(self.root1)
                self.root1.config(menu=m)
                filemenu=Menu(m,tearoff=0)
                m.add_cascade(label='Options', m=filemenu)
                filemenu.add_command(label='Full Statatics',command=DC.Show_Graphical_Performance)
                filemenu.add_command(label='Score Stats',command=DC.Show_Graphical_Performance_Score)
                filemenu.add_command(label='Balls Played Stats',command=DC.Show_Graphical_Performance_BallsPlayed)
                filemenu.add_command(label='Strike Rate Stats',command=DC.Show_Graphical_Performance_StrikeRate)
                filemenu.add_command(label='Exit',command=DC.Exit)

        #===========Frame-2================
                frame2=Frame(self.root1,bg='#2c2c2c')
                frame2.place(x=300,y=5,width=700,height=300)


        #=============Strike button===============
                strikechlb1=Label(frame2,bg='#2c2c2c',text="CHANGE STRIKE",fg="white",font=("",13,"bold")).place(x=550,y=90)

                strikebtn=Button(frame2,text=" Left ",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.strike)
                strikebtn.place(x=550,y=120)
                strike1btn=Button(frame2,text=" Right",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.strik)
                strike1btn.place(x=620,y=120)


        #===========Buttons================
                totalscrlb1=Label(frame2,bg='#2c2c2c',text="ADD SCORE",fg="white",font=("",13,"bold")).place(x=0,y=5)

                scr1btn=Button(frame2,text="+1",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.scr1)
                scr1btn.place(x=0,y=40)

                scr2btn=Button(frame2,text="+2",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.scr2)
                scr2btn.place(x=40,y=40)

                scr3btn=Button(frame2,text="+3",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.scr3)
                scr3btn.place(x=80,y=40)

                scr4btn=Button(frame2,text="+4",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.scr4)
                scr4btn.place(x=0,y=80)

                scr5btn=Button(frame2,text="+5",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.scr5)
                scr5btn.place(x=40,y=80)

                scr6btn=Button(frame2,text="+6",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.scr6)
                scr6btn.place(x=80,y=80)

                scrminusbtn=Button(frame2,text="-1 ",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.scrminus)
                scrminusbtn.place(x=40,y=120)

        #===========Wickets Label and Buttons================
                totalwktlb1=Label(frame2,bg='#2c2c2c',text="ADD WICKET",fg="white",font=("",13,"bold")).place(x=0,y=170)

                wktbtn=Button(frame2,text="+1",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.wicket)
                wktbtn.place(x=10,y=210)

                _wktbtn=Button(frame2,text="-1 ",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.wicketminus)
                _wktbtn.place(x=80,y=210)

        #==========Menu Selection Bar===============================
                def Out(self):
                        global out_reason,out_reason_checker
                        out_reason=var.get()
                        out_reason_checker=1

                var=StringVar(frame2)
                Out_Choices = {"Bold","RunOut","CatchOut","LBW","Hit-Wicket"}
                global Clear_Out_Reason
                var.set(Clear_Out_Reason)
                drop=OptionMenu(frame2,var,*Out_Choices,command=Out)
                drop.config(bg='black', fg ='white')
                drop.place(x=25,y=260)


        #===========BATSMAN_1 -Score Buttons================
                B1scrlb1=Label(frame2,bg='#2c2c2c',text="ADD B1 SCORE",fg="white",font=("",13,"bold")).place(x=200,y=5)

                B1scr1btn=Button(frame2,text="+1",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B1score1)
                B1scr1btn.place(x=200,y=40)

                B1scr2btn=Button(frame2,text="+2",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B1score2)
                B1scr2btn.place(x=240,y=40)

                B1scr3btn=Button(frame2,text="+3",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B1score3)
                B1scr3btn.place(x=280,y=40)

                B1scr4btn=Button(frame2,text="+4",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B1score4)
                B1scr4btn.place(x=200,y=80)

                B1scr5btn=Button(frame2,text="+5",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B1score5)
                B1scr5btn.place(x=240,y=80)

                B1scr6btn=Button(frame2,text="+6",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B1score6)
                B1scr6btn.place(x=280,y=80)

                B1scrminusbtn=Button(frame2,text="-1 ",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B1scoreminus)
                B1scrminusbtn.place(x=240,y=120)



        #===========BATSMAN_1 -Balls Played Buttons================
                B1ballplylb1=Label(frame2,bg='#2c2c2c',text="B1 BALLS PLAYED",fg="white",font=("",13,"bold")).place(x=200,y=170)

                B1ball1btn=Button(frame2,text="+1",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B1ballplay)
                B1ball1btn.place(x=200,y=210)

                B1ballminusbtn=Button(frame2,text="-1 ",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B1ballplayminus)
                B1ballminusbtn.place(x=280,y=210)


        #===========BATSMAN_2 -Score Buttons================
                B2scrlb1=Label(frame2,bg='#2c2c2c',text="ADD B2 SCORE",fg="white",font=("",13,"bold")).place(x=400,y=5)

                B2scr1btn=Button(frame2,text="+1",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B2score1)
                B2scr1btn.place(x=400,y=40)

                B2scr2btn=Button(frame2,text="+2",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B2score2)
                B2scr2btn.place(x=440,y=40)

                B2scr3btn=Button(frame2,text="+3",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B2score3)
                B2scr3btn.place(x=480,y=40)

                B2scr4btn=Button(frame2,text="+4",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B2score4)
                B2scr4btn.place(x=400,y=80)

                B2scr5btn=Button(frame2,text="+5",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B2score5)
                B2scr5btn.place(x=440,y=80)

                B2scr6btn=Button(frame2,text="+6",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B2score6)
                B2scr6btn.place(x=480,y=80)

                B2scrminusbtn=Button(frame2,text="-1 ",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B2scoreminus)
                B2scrminusbtn.place(x=440,y=120)



        #===========BATSMAN_2 -Balls Played Buttons================
                B2ballplylb1=Label(frame2,bg='#2c2c2c',text="B2 BALLS PLAYED",fg="white",font=("",13,"bold")).place(x=400,y=170)

                B2ball1btn=Button(frame2,text="+1",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B2ballplay)
                B2ball1btn.place(x=400,y=210)

                B2ballminusbtn=Button(frame2,text="-1 ",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.B2ballplayminus)
                B2ballminusbtn.place(x=480,y=210)

        #===========Total BALSS Increment  Buttons================
                t_ballslb1=Label(frame2,bg='#2c2c2c',text="ADD TOTAL BALLS",fg="white",font=("",11,"bold")).place(x=550,y=5)

                self.t_ballsbtn=Button(frame2,text="+1",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.t_balls)
                self.t_ballsbtn.place(x=550,y=40)

                self.t_ballsminusbtn=Button(frame2,text="-1 ",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.t_ballsminus)
                self.t_ballsminusbtn.place(x=650,y=40)

        #==========================Clear Button=====================
                self.clear=Button(frame2,text="Clear",bg='#2c2c2c',fg="white",font=("",15,"bold"),command=app.Clear)
                self.clear.place(x=590,y=210)

        #==================Automatic CheckBox=======================
                def Auto():
                        global auto_checker,evod
                        evod+=1
                        if(evod%2==0): auto_checker=1
                        else: auto_checker=0
                var_check=IntVar()
                self.auto=Checkbutton(frame2,text="Automatic",variable=var_check,bg='grey',fg="black",font=("",15,"bold"),command=Auto)
                self.auto.place(x=575,y=265)

        #===========Frame-3================
                frame3=Frame(self.root1,bg='#2c2c2c')
                frame3.place(x=300,y=350,width=700,height=150)

                t_over1b1=Label(frame3,text="Enter Total Overs",bg='#2c2c2c',fg="white",font=("",11,"bold")).place(x=10,y=20)

                self.t_overentry=Entry(frame3,bg='#2c2c2c',fg="white",font=("",10,"bold"))
                self.t_overentry.place(x=10,y=50)

                t_overbtn=Button(frame3,text="UPDATE",bg='#2c2c2c',fg="white",font=("",12,"bold"),command=app.over_update)
                t_overbtn.place(x=40,y=100)


                B1name1b1=Label(frame3,text="Enter BATSMAN-1",bg='#2c2c2c',fg="white",font=("",11,"bold")).place(x=170,y=20)

                self.B1name_entry=Entry(frame3,bg='#2c2c2c',fg="white",font=("",10,"bold"))
                self.B1name_entry.place(x=170,y=50)

                B1namebtn=Button(frame3,text="UPDATE",bg='#2c2c2c',fg="white",font=("",12,"bold"),command=app.B1name_update)
                B1namebtn.place(x=210,y=100)

                B2name1b1=Label(frame3,text="Enter BATSMAN-2",bg='#2c2c2c',fg="white",font=("",11,"bold")).place(x=330,y=20)

                self.B2name_entry=Entry(frame3,bg='#2c2c2c',fg="white",font=("",10,"bold"))
                self.B2name_entry.place(x=330,y=50)

                B2namebtn=Button(frame3,text="UPDATE",bg='#2c2c2c',fg="white",font=("",12,"bold"),command=app.B2name_update)
                B2namebtn.place(x=370,y=100)

                teamname1b1=Label(frame3,text="Enter TEAM NAME",bg='#2c2c2c',fg="white",font=("",11,"bold")).place(x=490,y=20)

                self.teamname_entry=Entry(frame3,bg='#2c2c2c',fg="white",font=("",10,"bold"))
                self.teamname_entry.place(x=490,y=50)

                teamnamebtn=Button(frame3,text="UPDATE",bg='#2c2c2c',fg="white",font=("",12,"bold"),command=app.teamname_update)
                teamnamebtn.place(x=530,y=100)


class DataControl:
        def Excel(self):
                global score2,score3,ballsplayed,ballsplayed2,Strike_Pointer,wickets,Strike_List,CSV_checker
                if(CSV_checker==0):
                        with open("E:\\Python GUI Project\\Data.csv","w") as csvfile:
                                writer=csv.writer(csvfile)
                                writer.writerow(["Player Name","Score","Balls Played","Strike Rate"])
                                csvfile.close()
                                CSV_checker=1

                with open("E:\\Python GUI Project\\Data.csv","a") as csvfile:
                        writer=csv.writer(csvfile)
                        if(Strike_Pointer==0):
                                Strike_Rate=(score2/ballsplayed)*100
                                writer.writerow([Strike_List[0],score2,ballsplayed,Strike_Rate])
                                csvfile.close()
                        else:
                                Strike_Rate=(score3/ballsplayed2)*100
                                writer.writerow([Strike_List[1],score3,ballsplayed2,Strike_Rate])
                                csvfile.close()

        def End_Excel(self):
                global score2,score3,ballsplayed,ballsplayed2,Strike_Pointer,wickets,Strike_List,CSV_checker
                if(CSV_checker==0):
                        with open("E:\\Python GUI Project\\Data.csv","w") as csvfile:
                                writer=csv.writer(csvfile)
                                writer.writerow(["Player Name","Score","Balls Played","Strike Rate"])
                                csvfile.close()
                                CSV_checker=1

                with open("E:\\Python GUI Project\\Data.csv","a") as csvfile:
                        writer=csv.writer(csvfile)
                        Strike_Rate1=(score2/ballsplayed)*100
                        Strike_Rate2=(score3/ballsplayed2)*100
                        writer.writerow([Strike_List[0],score2,ballsplayed,Strike_Rate1])
                        writer.writerow([Strike_List[1],score3,ballsplayed2,Strike_Rate2])
                        csvfile.close()
                

        def Show_Graphical_Performance(self):
                d=read_csv("E:\\Python GUI Project\\Data.csv")
                Name=d['Player Name'].tolist()
                sc=d['Score'].tolist()
                BP=d['Balls Played'].tolist()
                SR=d['Strike Rate'].tolist()

                plt.plot(Name,sc,label='Score',marker='o',Linestyle='--')
                plt.plot(Name,BP,label='Balls Played',marker='o',Linestyle='--')
                plt.plot(Name,SR,label='Strike Rate',marker='o',Linestyle='--')
                plt.title('Cricket')
                plt.xlabel('Name')
                plt.ylabel('Performance')
                plt.legend(loc="upper left")
                plt.show()
               
        def Show_Graphical_Performance_Score(self):
                d=read_csv("E:\\Python GUI Project\\Data.csv")
                Name=d['Player Name'].tolist()
                sc=d['Score'].tolist()
                BP=d['Balls Played'].tolist()
                SR=d['Strike Rate'].tolist()

                plt.plot(Name,sc,label='Score',marker='o',Linestyle='--')
                plt.title('Cricket')
                plt.xlabel('Name')
                plt.ylabel('Score')
                plt.legend(loc="upper left")
                plt.show()

        def Show_Graphical_Performance_BallsPlayed(self):
                d=read_csv("E:\\Python GUI Project\\Data.csv")
                Name=d['Player Name'].tolist()
                sc=d['Score'].tolist()
                BP=d['Balls Played'].tolist()
                SR=d['Strike Rate'].tolist()

                plt.plot(Name,BP,label='Balls Played',marker='o',Linestyle='--',color='orange')
                plt.title('Cricket')
                plt.xlabel('Name')
                plt.ylabel('Balls Played')
                plt.legend(loc="upper left")
                plt.show()

        def Show_Graphical_Performance_StrikeRate(self):
                d=read_csv("E:\\Python GUI Project\\Data.csv")
                Name=d['Player Name'].tolist()
                sc=d['Score'].tolist()
                BP=d['Balls Played'].tolist()
                SR=d['Strike Rate'].tolist()

                plt.plot(Name,SR,label='Strike Rate',marker='o',Linestyle='--',color='green')
                plt.title('Cricket')
                plt.xlabel('Name')
                plt.ylabel('Strike Rate')
                plt.legend(loc="upper left")
                plt.show()
         

        def Exit(self):
                exit()


DC=DataControl()
root=Tk()
root1=Tk()
app=Destination(root)
app1=Datastation(root1)
root.mainloop()
root1.mainloop()
