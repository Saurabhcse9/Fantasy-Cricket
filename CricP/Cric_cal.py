#Batting and Bowling score calculation


def bb_score(Scored,Faced,Fours,Sixes,Bowled,Given,Wkts,Catches,Stumping,RO):
    score=0
    overs=Bowled/6
    strike_rate=0
    try:
        strike_rate=Scored/Faced*100
    except:
        pass

    score=score+Wkts*10 #10 points for each wicket
    if Wkts>=3:
        score=score+5 # Additional 5 points for three wickets in innings
    if Wkts>=5:
        score=score+10  # Additional 10 points for 5 wickets or more in innings
    if overs>0:
        economy_rate=Given/overs
        if economy_rate>=3.5 and economy_rate<=4.5:
            score=score+4  #4 Points for economy rate between 3.5 and 4.5
        if economy_rate>2 and economy_rate<3.5:
            score=score+7  #7 Points for economy rate between 2 and 3.5
        if economy_rate<=2:
            score=score+10  #10 Points for economy rate less than 2
    
    
    if Scored!=0:
        score=score+int(Scored/2) #1 point for 2 run scored
    if Scored>50:
        score=score+5 # Additional 5 points for a half-century
    if Scored!=0:
        score=score+int(Scored/100)*10 # Additional 10 points for a century
        
    if strike_rate>=80 and strike_rate<=100:               
        score=score+2  #2 Points for strike rate of 80-100
        
    if strike_rate>100:
        score=score+4  #Additional 4 points for strike rate>100
                       
    score=score+Fours  #1 point for hitting a boundary
                   
    score=score+Sixes*2  #2 points for hitting over boundary
        
    score=score+(Catches+Stumping+RO)*10


    return score


#Test your result
#score=bb_score(0,0,0,0,60,45,2,0,0,0)
#print(score)
        
    

