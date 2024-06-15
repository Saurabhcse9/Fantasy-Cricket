#Python Fantasy Cricket Project for 
#Completed Under Guidence of INTERNSHALA
#Detail:from Institute of Engineering and Technology Lucknow has successfully completed a six weeks online
#training on Programming with Python from 20th June, 2020 to 1st August, 2020

import sqlite3
import sys
from Game_Window import *
from NO_TEAM import *
from Evaluate import *
from Error_Message import *
from Cric_cal import *
from about import *
from Instructions import *
from Party import *

Cric_db=sqlite3.connect('CricP.db')   #Connecting to Cricket DATABASE Cric_db
cric=Cric_db.cursor()

class Driver:
    def __init__(self):         #Initial Setup       
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.showMaximized()
        try:                               
            self.Select_P=[]
            self.Selected_P=[]
            self.BAT=0
            self.BWL=0
            self.AR=0
            self.WK=0
            self.Value=0
            self.team_name=''
            self.ui.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)
            self.ui.menuHelp.triggered[QtWidgets.QAction].connect(self.help)
            self.ui.BAT_RB.toggled.connect(self.Show_Bat)
            self.ui.BOW_RB.toggled.connect(self.Show_Bow)
            self.ui.AR_RB.toggled.connect(self.Show_AR)
            self.ui.WK_RB.toggled.connect(self.Show_WK)
            self.ui.Select_P.itemDoubleClicked.connect(self.removelist1)
            self.ui.Selected_P.itemDoubleClicked.connect(self.removelist2)
            self.dis_RL()
        except:
            print("Error....")
        sys.exit(self.app.exec_())
        
    def menufunction(self, action):    #Manages NEW TEAM, OPEN TEAM, SAVE TEAM, EVALUATE TEAM FOR MANAGE 
         txt= (action.text())
         if txt =='New Team':
            self.ui.PA_LB.setText(str(Total))
            self.noTeam('0')
         if txt=='Open Team':
            print("Opening")
            self.noTeam('1')
         if txt =='Save Team':
            print("Saving...")
            if self.ui.Selected_P.count()==11 and self.ui.WK_LB.text()=='1':
                self.delete()
            self.start_it()
         if txt=='Evaluate Team':
            print("Evaluating..")
            self.eval()

    def help(self, action):      #Manages ABOUT, INSTRUCTIONS 
        txt= (action.text())
        if txt =='About':
            self.ui.ABOUT = QtWidgets.QDialog(self.MainWindow)
            self.ui.AboutUi = Ui_ABOUT()
            self.ui.AboutUi.setupUi(self.ui.ABOUT)
            self.ui.ABOUT.show()
        if txt =='Instructions':
            self.ui.Dialog = QtWidgets.QDialog(self.MainWindow)
            self.ui.dUi = Ui_Dialog()
            self.ui.dUi.setupUi(self.ui.Dialog)
            self.ui.Dialog.show()
            
    def noTeam(self,a):              #OPENS EXISTING TEAM OR CREATES A NEW TEAM
        self.ui.Saved_LB.setText('')
        self.dis_RL()
        self.ui.NO_TEAM = QtWidgets.QDialog(self.MainWindow)
        self.ui.getNameUi = Ui_NO_TEAM()
        self.ui.getNameUi.setupUi(self.ui.NO_TEAM)
        self.ui.NO_TEAM.show()
        self.ui.getNameUi.OK_PB.clicked.connect(lambda:self.intiate(a))

    def eval(self):                 #EVALUATES A EXISTING TEAM
        self.dis_RL()
        self.ui.Evaluate = QtWidgets.QDialog(self.MainWindow)
        self.ui.evaluateUi = Ui_Evaluate()
        self.ui.evaluateUi.setupUi(self.ui.Evaluate)
        self.ui.Evaluate.show()
        q='''SELECT MatchID FROM MATCH;'''
        x='''SELECT Team_Name FROM TEAMS '''
        a=self.Cblst(q)
        b=self.Cblst(x)
        self.AddCb(a,1)
        self.AddCb(b,0)
        self.ui.evaluateUi.Team_Select_CB.activated.connect(self.popeval)
        self.ui.evaluateUi.Eval_PB.clicked.connect(self.calc)
        self.ui.evaluateUi.OkEval_PB.clicked.connect(self.stopev)

    def stopev(self):
        self.ui.Evaluate.close()

    def calc(self):   #CALCULATES SCORE FOR EVALUATION
        lst=[]
        print("Calculating......")
        y=self.ui.evaluateUi.Players_lst
        for x in range(y.count()):
            lst.append(y.item(x).text())
        self.popscore(lst)
        self.Cong(self.ui.evaluateUi.Score_Lb.text())

    def Cong(self,a):   #DISPLAYS A CONGRATULATION MESSAGE IF A TEAM EVALUATED SCORES HIGHEST
        print("in")
        h=0
        p=''' SELECT Score FROM SCORE WHERE Score=?;'''
        cric.execute(p,(int(a),))
        record=cric.fetchone()
        if record==None:
            q='''INSERT INTO SCORE (Score) VALUES (?); '''
            cric.execute(q,(int(a),))
            Cric_db.commit()
        cric.execute('''SELECT Score FROM SCORE''')
        while True:
            z=cric.fetchone()
            if z==None:
                break
            elif int(a)>=z[0]:
                h=1
            else:
                h=0
        if h==1:
            print("inn")
            self.ui.Party = QtWidgets.QDialog(self.MainWindow)
            self.ui.pUi = Ui_Party()
            self.ui.pUi.setupUi(self.ui.Party)
            self.ui.Party.show()
            
    def popscore(self,lst):     #Populates Score and Various Labels for EVALUATE WINDOW
        t=0
        v=0
        self.ui.evaluateUi.Point_lst.clear()
        q='''SELECT Scored,Faced,Fours,Sixes,Bowled,Given,Wkts,Catches,Stumping,RO,Value
             FROM MATCH JOIN STATS ON STATS.PlayerID=MATCH.PlayerID WHERE Player_Name=? AND MatchID=?;'''
        for i in lst:
            cric.execute(q,(i,'MATCH1',))
            record=cric.fetchone()
            score=bb_score(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9])
            t+=score
            v+=record[10]
            self.ui.evaluateUi.Points_Lb.setText(str(v))
            self.ui.evaluateUi.Point_lst.addItem(str(score))
        self.ui.evaluateUi.Score_Lb.setText(str(t))
    def er(self,text):
        self.ui.Error_Message = QtWidgets.QDialog(self.MainWindow)
        self.ui.erUi = Ui_Error_Message()
        self.ui.erUi.setupUi(self.ui.Error_Message)
        self.ui.erUi.Oh_No_Message.setText(text)
        self.ui.Error_Message.show()
        self.ui.erUi.OKEr_PB.clicked.connect(self.stopMB)
        
    def Show_Bat(self):
        if self.ui.BAT_RB.isChecked()==True:
            self.ui.Select_P.clear()
            self.Paint("BAT")

    def Show_Bow(self):
        if self.ui.BOW_RB.isChecked()==True:
            self.ui.Select_P.clear()
            self.Paint("BWL")

    def Show_AR(self):
        if self.ui.AR_RB.isChecked()==True:
            self.ui.Select_P.clear()
            self.Paint("AR")

    def Show_WK(self):
        if self.ui.WK_RB.isChecked()==True:
            self.ui.Select_P.clear()
            self.Paint("WK")

    def removelist1(self, item):
        self.labels()
        r=0
        r=self.results()
        if r==1:
            self.ui.Select_P.takeItem(self.ui.Select_P.row(item))
            self.ui.Selected_P.addItem(item.text())
            self.labels()
    def removelist2(self, item):
        a=self.ui.Selected_P.currentItem().text()
        self.ui.Selected_P.takeItem(self.ui.Selected_P.row(item))
        q=''' SELECT ctg FROM MATCH JOIN STATS ON STATS.PlayerID=MATCH.PlayerID WHERE Player_Name=?;'''
        try:
            cric.execute(q,(a,))
            record=cric.fetchone()
            if self.ui.BAT_RB.isChecked()==True and record[0]=="BAT":
                self.ui.Select_P.addItem(item.text())
            elif self.ui.BOW_RB.isChecked()==True and record[0]=="BWL":
                self.ui.Select_P.addItem(item.text())
            elif self.ui.AR_RB.isChecked()==True and record[0]=="AR":
                self.ui.Select_P.addItem(item.text())
            elif self.ui.WK_RB.isChecked()==True and record[0]=="WK":
                self.ui.Select_P.addItem(item.text())
            else:
                pass
        except:
            pass
        self.labels()

    def intiate(self,a):
        self.team_name=self.ui.getNameUi.Team_Name_Edit.text()
        if a=='0':
            if self.team_name=='' or self.team_name==' ' or self.team_name[0:2]=='  ':
                text="Please Enter Your Team Name \n          Properly!"
                self.er(text)
            else:
                self.open(a)
        else:
            self.open(a)
        self.ui.NO_TEAM.close()

    def stopMB(self):
        self.ui.Error_Message.close()

    def start_it(self):
        if self.ui.Select_P.isEnabled()==True:
            if self.BAT+self.AR+self.WK+self.BWL<11:
                txt='I Guess we need...\n   11 Players'
                self.er(txt)
            elif self.WK==0:
                txt='Oops!! We forgot, we have no\n      WICKET KEEPER'
                self.er(txt)
            else:
                self.save()
        else:
            txt="        No Team ? ...\n\nDon't worry!,Create a New Team..\n            Say\n        Internshala11"
            self.er(txt)


    def enClear(self):
        self.ui.BAT_RB.setEnabled(True)
        self.ui.BOW_RB.setEnabled(True)
        self.ui.AR_RB.setEnabled(True)
        self.ui.WK_RB.setEnabled(True)
        self.ui.Select_P.setEnabled(True)
        self.ui.Selected_P.setEnabled(True)

    def dis_RL(self):
        self.BAT=0
        self.BWL=0
        self.AR=0
        self.WK=0
        self.Value=0
        self.team_name=''
        self.ui.BAT_RB.setEnabled(False)
        self.ui.BOW_RB.setEnabled(False)
        self.ui.AR_RB.setEnabled(False)
        self.ui.WK_RB.setEnabled(False)
        self.ui.Select_P.setEnabled(False)
        self.ui.Selected_P.setEnabled(False)
        self.ui.BAT_RB.setChecked(False)
        self.ui.BOW_RB.setChecked(False)
        self.ui.AR_RB.setChecked(False)
        self.ui.WK_RB.setChecked(False)
        self.ui.Select_P.clear()
        self.ui.Selected_P.clear()
        self.Selected_P.clear()
        self.Select_P.clear()
        self.ui.PA_LB.setText("####")
        self.ui.PU_LB.setText("####")
        self.ui.BAT_LB.setText("##")
        self.ui.BOW_LB.setText("##")
        self.ui.AR_LB.setText("##")
        self.ui.WK_LB.setText("####")
        self.ui.Team_Name.setText("Your Team")

    def Paint(self,ctg):   #Populates GAME WINDOW
        q=''' SELECT Player_Name FROM MATCH JOIN STATS ON STATS.PlayerID=MATCH.PlayerID WHERE ctg=?;'''
        cric.execute(q,(ctg,))
        while True:
            record=cric.fetchone()
            if record==None:
                break
            x=self.ui.Selected_P
            self.extract(x)
            if record[0] not in items:
                self.ui.Select_P.addItem(record[0])

    def extract(self,y):    #Returns a list of items from a QlistWidget
        items.clear()
        for x in range(y.count()):
            items.append(y.item(x).text())
        return items

    def labels(self):      #Poplates various labels in GAME WINDOW
        self.BAT=0
        self.BWL=0
        self.AR=0
        self.WK=0
        self.Value=0
        q='''SELECT Value,ctg FROM MATCH JOIN STATS ON
             STATS.PlayerID=MATCH.PlayerID WHERE Player_Name=?;'''
        y=self.ui.Selected_P
        self.extract(y)
        for i in items:
            cric.execute(q,(i,))
            record=cric.fetchone()
            if record==None:
                break
            if record[1]=="BAT":
                self.BAT+=1
                self.ui.BAT_LB.setText(str(self.BAT))
            elif record[1]=="BWL":
                self.BWL+=1
                self.ui.BOW_LB.setText(str(self.BWL))
            elif record[1]=="AR":
                self.AR+=1
                self.ui.AR_LB.setText(str(self.AR))
            elif record[1]=="WK":
                self.WK+=1
                self.ui.WK_LB.setText(str(self.WK))
            else:
                pass
            self.Value+=record[0]
        self.ui.PA_LB.setText(str(Total-self.Value))
        self.ui.PU_LB.setText(str(self.Value))
        self.ui.BAT_LB.setText(str(self.BAT))
        self.ui.BOW_LB.setText(str(self.BWL))
        self.ui.AR_LB.setText(str(self.AR))
        self.ui.WK_LB.setText(str(self.WK))

    def results(self):                 #CHECKS VARIOUS CONDITONS PRIOR TO SAVING A TEAM
        if self.BAT==4 and self.ui.BAT_RB.isChecked()==True:
            text="Oops!!.....Not more than\n    4 BATSMEN"
            self.er(text)
        elif self.BWL==3 and self.ui.BOW_RB.isChecked()==True:
            text="Oh NO!!..Not more than\n      3 BOWLERS"
            self.er(text)
        elif self.WK==1 and self.ui.WK_RB.isChecked()==True:
            text="Oh NO!!..Not more than\n      1 WICKET-KEEPER"
            self.er(text)
        elif self.BAT+self.BWL+self.AR+self.WK==11:
            text="Oh NO!!..Not more than\n      11 Players"
            self.er(text)
        else:
            return 1

    def save(self):
        y=self.ui.Selected_P
        f_lst=self.extract(y)
        R=''' INSERT INTO TEAMS(Team_Name,PlayerID,Value) VALUES (?,?,?);'''
        Q='''SELECT Value FROM STATS WHERE PlayerID=?; '''
        p=''' SELECT PlayerID FROM MATCH WHERE Player_Name=?; '''
        n=self.team_name
        try:
            for i in f_lst:
                cric.execute(p,(i,))
                record=cric.fetchone()
                cric.execute(Q,(record[0],))
                val=cric.fetchone()
                cric.execute(R,(n,record[0],val[0]))
                Cric_db.commit()
            self.ui.Saved_LB.setText("Saved successfully....")
            self.dis_RL()
        except:
            print("Failed")

    def Checkif(self,n):
        q='''SELECT Team_Name FROM TEAMS WHERE Team_name=?;'''
        cric.execute(q,(n,))
        record=cric.fetchone()
        if record==None:
            return 1
        else:
            return 0

    def open(self,a):
        txt1='Great name choice...but it\n Team already exists'
        txt2='Great name choice but... \nTeam not found, Try Again!!'
        temp=self.Checkif(self.team_name.lower())
        if temp==1 and a=='0':
           self.setup()
        elif a=='0':
            self.er(txt1)
        elif temp==1 and a=='1':
            self.er(txt2)
        else:
            self.setup()
            self.populate()

    def setup(self):
        self.enClear()
        self.ui.Team_Name.setText(self.team_name)
        self.team_name=self.team_name.lower()

    def delete(self):
        q='DELETE FROM TEAMS WHERE Team_Name=?;'

        try:
            cric.execute(q,(self.team_name,))
            Cric_db.commit()
        except:
            pass

    def populate(self):
        q='SELECT Player_Name  FROM MATCH JOIN TEAMS ON TEAMS.PlayerID=MATCH.PlayerID WHERE Team_Name=?;'
        try:
            cric.execute(q,(self.team_name,))

            while True:
                record=cric.fetchone()
                if record==None:
                    break
                self.ui.Selected_P.addItem(record[0])
            self.labels()
        except:
            pass

    def popeval(self):
         self.ui.evaluateUi.Players_lst.clear()
         q='''SELECT Player_Name  FROM MATCH JOIN TEAMS ON TEAMS.PlayerID=MATCH.PlayerID WHERE Team_Name=?;'''
         try:
            cric.execute(q,(self.ui.evaluateUi.Team_Select_CB.currentText(),))
            while True:
                record=cric.fetchone()
                if record==None:
                    break
                self.ui.evaluateUi.Players_lst.addItem(record[0])
         except:
             pass

    def Cblst(self,q): 
        lst=[]
        try:
            cric.execute(q)

            while True:
                temp=0
                record=cric.fetchone()
                if record==None:
                    break
                elif len(lst)==0:
                    lst.append(record[0])
                elif lst[temp-1]!=record[0]:
                    lst.append(record[0])
                else:
                    pass
                temp+=1
        except:
             pass
        return lst

    def AddCb(self,x,y):
        for i in x:
            if y==1:
                self.ui.evaluateUi.Match_Select_CB.addItem(i)
            else:
                self.ui.evaluateUi.Team_Select_CB.addItem(i)
            
if __name__=="__main__":    #DRIVER
    items=[]
    Total=0
    q=''' SELECT Value FROM STATS;
        '''
    cric.execute(q)
    
    while True:
        record=cric.fetchone()
        if record==None:
            break
        Total+=record[0]
    G=Driver()                 
            
            
