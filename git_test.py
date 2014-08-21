<pre class="brush:python;"> 
>>> import PyGithub
>>> g_inst = PyGithub.BlockingBuilder().Build()     # github instance 
>>> user = g_inst.get_user("jayu108")    # github id
>>> print user.name                 # github id 에 해당하는 이름 출력
park
>>> repo = user.get_repo("biopython")   # github id 소유의 repository 이름
>>> print repo.stargazers_count
0
>>> 
</pre>



<pre class="brush:python;"> 

</pre>



rr = user.get_repos()   # user 소유 repository 이름 모두 얻기.

for repo in rr:
	print repo.full_name   # repository 이름 출력
	print repo.description   # repository 설명 -- README.md 내용

	
	
gg = user.get_gists()   # user 소유 gist 이름 모두 얻기. (public만 ?)

for gist in gg:
	print gist.id     # gist id 출력

	
# http://jacquev6.github.io/PyGithub/v2/reference/classes/User.html#PyGithub.Blocking.User.User.update
user.update()    # user 정보 갱신

print user.email   # github 에 등록한 e-mail 출력.

print user.html_url  # 사용자 github url 출력.




****** 사용자 본인 인증 접속하기 ******

g_inst = PyGithub.BlockingBuilder().Login("bioinfo_id", "12345678_pass").Build()
user = g_inst.get_authenticated_user()

print user.login
print user.name
print user.email
print user.id


rr = user.get_repos()

	
for repo in rr:
	print repo.name
	print repo.full_name
	print repo.description
	repo.created_at
	repo.updated_at
	try:
		cnts = repo.get_contents("")
		# file document
		# http://jacquev6.github.io/PyGithub/v2/reference/classes/File.html#PyGithub.Blocking.File.File		
		for c in cnts:
			print c.name, c.size, c.type, c.url
			print ' 1------------ '
			if c.type == u'file' :print c.content
			print ' 2------------ '
			print c.html_url			
	except :
		print '-- no contents --'
	# x.creator
	print
	
	

