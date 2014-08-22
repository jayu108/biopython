import PyGithub
import base64

g_inst = PyGithub.BlockingBuilder().Login("jayu108", "123456").Build()
user = g_inst.get_authenticated_user()

print user.login
print user.name
print user.email
print user.id
print 

rr = user.get_repos()

        
for repo in rr:
        print repo.name
        print repo.full_name
        print repo.description
        print ' repo.created_at ==> ', repo.created_at
        print ' repo.updated_at ==> ',repo.updated_at
        print ' repo.downloads_url  = ', repo.downloads_url
        print ' repo.html_url ==> ',  repo.html_url
        print ' repo.owner ==> ', repo.owner
        print ' repo.pulls_url ==> ', repo.pulls_url
        print ' repo.pushed_at ==> ', repo.pushed_at
        print ' repo.size ==> ', repo.size
        print ' repo.ssh_url ==> ', repo.ssh_url
        print ' repo.statuses_url ==> ', repo.statuses_url

        print ' repo.get_keys ==> ', repo.get_keys()
        
        print '         ===============         '
##        try:
##                cnts = repo.get_contents("")
##                # file document
##                # http://jacquev6.github.io/PyGithub/v2/reference/classes/File.html#PyGithub.Blocking.File.File         
##                for c in cnts:
##                        print c.name, c.size, c.type, c.html_url
##                        print ' 1------------ '
##                        if c.type == u'file' :
##                                # print c.content   # base64 encoding  --  https://developer.github.com/v3/repos/contents/#contents
##                                print base64.b64decode(c.content)
##                        print ' 2------------ '
##                        print c.html_url                        
##        except :
##                print '-- no contents --'
        # x.creator
        print



# repo.delete()    # delete repository !!!!


# user.create_repo('test_bio11', 'test bio 11')   # create new repository !!


repo1 , repo2 = rr[0] , rr[1]

print repo1
print repo2
print repo1.full_name
print repo2.full_name


print 'before => ', repo2.description

# repository name , description 변경
# https://developer.github.com/v3/repos/#edit
# http://jacquev6.github.io/PyGithub/v2/reference/classes/Repository.html#PyGithub.Blocking.Repository.Repository.edit
repo2.edit( name = 'test_bio22', description = 'test repo edit 333..')  
print 'after => ', repo2.description
print


cm = repo1.get_commits() # PaginatedList of Commit
cmt = repo1.get_commit_comments()  # comments list

print cm
print cmt

print ' ******************************************************* '

for commit in cm:
    ##    print'  commit -- ', commit
    ##    commit.files     # list of files
    ##    sts = commit.get_statuses()  # PaginatedList of Commit.Status
    ##    print 'sts -- ', sts
    ##    # print ' len of sts == ', len(sts)
    ##    for st in sts:
    ##        print '.....'
    ##        print st
    ##        print 'commit status  ==> ', st.created_at, st.updated_at, st.description
    for x in commit.files:
        # print x      # file object
        print x.filename , x.changes, x.status, x.sha
        
    print '  -------- '

print ' ******************************************************* '


for comment in cmt:  # ???????
    print comment


# http://jacquev6.github.io/PyGithub/v2/reference/classes/Repository.html#PyGithub.Blocking.Repository.Repository.create_file
# 현재 repository (repo1) 에 , directroy 명 'dir_name' 아래 'test.txt' 라는
# 파일을 만드는데, 그 파일 내용은 base64로 인코딩된 'ZGF0YSB0byBiZSBlbmNvZGVk' 이다.
repo1.create_file('dir_name/test.txt', '1st create file test','ZGF0YSB0byBiZSBlbmNvZGVk')



with open('tt.py') as f:
    

    


