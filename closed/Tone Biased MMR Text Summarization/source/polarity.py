from textblob import TextBlob as tb

doc="60"
#mmr_summary 
x= """;   
Witnesses back King's version of what happened early Sunday morning in a Los
Angeles suburb, and a CHP officer at the scene said he exhorted the police
officers to stop the beating, but was told, in effect, to "stay out of it,"
according to a source. "I would hope the public
on this one case not make a judgment on the Los Angeles Police Department. ;    On his recent visits, he said, King
was having difficulty remembering the night of the beating in a coherent way. ;    Los Angeles
Traffic Detective Richard Talkington told the Los Angeles Times that written
police reports from officers involved said King ignored several requests to
leave the car after he was stopped. 

"""

#human_summary 
y ="""Rodney King, of Los Angeles, was stopped after a high speed chase on
June 6.  After leaving his car he was held down and beaten by a number
of policemen, suffering a broken jaw, broken leg and numerous bruises
in the encounter, requiring hospital treatment. Mr. King denied
driving at high speeds and stated he was struck at least forty times
as he begged police to stop.  Police claim King resisted arrest, but
witnesses deny this.  The entire incident was videotaped by a
bystander and released to the media, creating a furor throughout the
country.

Bryant Allen, one of Mr. King's passengers, claims he, too was
racially provoked and forced to crawl on the ground as King was
beaten.  Another passenger agrees.  Mr. Allen says that the three, all
black, had consumed some beer, but no drugs.  Tests confirmed this.

Police say that 21 officers were present as King was shot with a stun
gun and then beaten.  Two Highway Patrol officers who were present
protested, but were ordered off the case by local police.

Police officials, the FBI and the District Attorney are investigating.
An ACLU spokesman said that these incidents "happen all the time," and
black Los Angeles residents agree.

Although the police wanted to charge King with battery on an officer and 
resisting arrest, the DA refused, sending the case back to police for further 
investigation.  The ten officers involved were taken off patrol and four, a 
sergeant and three other officers, have been indicted for assault.  Mr. Allen 
and the other passenger are bringing civil rights suits against the police.  
Neither Mr. King nor his passengers have been charged.

Some policemen who watched King's beating maintain the arrest was done
correctly and a Grand Jury has declined to indict them for their
inaction.  The District Attorney is forwarding the "disturbing
interviews" with bystanding officers to the local independent
commission investigating the police department, and Chief Darryl Gates
has fired one police rookie and suspended three others.

Rodney King, released from jail without charges, spends his time
seeing doctors and worrying about his health.  He required a four hour
plastic surgery to repair his shattered cheek and jaw, and suffers
from numbness of the face and headaches.  Depressed and frightened, he
is guarded as he stays with relatives, and has instituted an $83
million suit against the city for excessive force.  Because of the
extensive publicity, he has been identified as a suspect in a recent
robbery.
"""


print doc, (tb(x).sentiment.polarity), (tb(y).sentiment.polarity)