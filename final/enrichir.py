import sys,re

if len(sys.argv)!=2:
	print("Vous devez entrer le nom du corpus")
else:	

	def FRordre(str1,str2):
		b=["a","b","c","d","e","é","è","ê","f","g","h","i","ï","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		
		p1=0
		
		while p1<len(str1) and p1<len(str2):
			
			if b.index(str1[p1]) > b.index(str2[p1]):
				return True
			
			if b.index(str1[p1]) < b.index(str2[p1]):
				return False
				
			else:
				p1=p1+1
		
		if(len(str1)<=len(str2)):
			return False
		
		else:
			return True
		 
	

	substEnri=open("subst_enri.dic",'w',encoding="utf-16")
	substEnri.write("\ufeff")

	subst=open("subst.dic",'r',encoding="utf-16")
	Lsubst=subst.readlines()
	subst.close()
	
	
	
	fcorpus=open(sys.argv[1],'r',encoding="utf-8")
	corpus=fcorpus.readlines()
	fcorpus.close()

	regex=r"^([^A-Za-z]| ){0,3}(\w+) :? ?(LP)?(\d+|\.|,)+ (mg|ml)".encode("utf-16").decode("utf-16")

	cpt=1
	dicenr={}
	alpha={}
	
	for j in corpus:
		j=j.encode("utf-16-le").decode("utf-16-le")
		medocs=re.findall(regex,j,re.I)
		
		if len(medocs)!=0: 
			m=medocs[0][1].lower()+",.N+subst\n"
			
			substEnri.write(m)
			
			dicenr[m]=dicenr.get(m,0)+1
			
			if  (dicenr[m]==1)  and  not(m in Lsubst):
				
				p=0
				while p<len(Lsubst) and FRordre(m,Lsubst[p]):
					p=p+1
				
				if p<len(Lsubst):
					Lsubst.insert(p,m)
				
				alpha[m[0]]=alpha.get(m[0],0)+1
				
			print(str(cpt)+" "+medocs[0][1])
			cpt=cpt+1
		
		
	substEnri.close()
	
	subst=open("subst.dic",'w',encoding="utf-16-le")
	subst.write("\ufeff")
	for j in Lsubst:
		subst.write(j)
	subst.close()
	
	info2=open("info2.txt",'w',encoding="utf-16")
	
	cpt=0
	for j in sorted(alpha):
		info2.write(j+": "+str(alpha.get(j))+"\n")
		cpt=cpt+alpha.get(j)
	
	info2.write("\nTotal: "+str(cpt))	
		
	info2.close()

