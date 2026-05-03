ssis package to push claims to a database
stored procedure to propose and autopay or autdeny or auto pend depending on business rules. ]

busiess rules in stored procedures
make sure their applied

config arch create drg config  and load

inclusions criteria 
de inclusion criteria

process and put in the system

any drg code coming from provider has to be denied

recieve the claim look at the claims what is submitted drg codes and provider data is matching

next step deny

once its denied

once a claim has been denied no down stream impact wont be touched

paid it will go to cotivity no impact might be regression only

apr dgr quest these are different tables
ms drg pb mcr these are different tables

-----                                                                         
  Hi team,                                                                                                                                                  
  I spent some time going through the test plan and wanted to share what I    
  found and get some clarity on a few things before standup.                  
                                                                              
  I mapped out everything in the test repo — 19 test cases total across SIT
  and UAT. The SIT side covers file processing pretty well (file exists, happy   path, missing columns, email, reconciliation, archive, etc.) but the
  exclusion file only has 4 TCs compared to the mapping file's 10. I've         identified 11 gaps on the exclusion file side that need to be added, mostly
  around negative scenarios like file not found, access denied, corrupt files,
   duplicate keys, and update/terminate scenarios.
  
  The bigger thing I noticed is that all our current test cases cover one
  layer — file processing. Did the job run, did data load, did the email send.
   But there are three more layers I think we should be considering:
                                                                                File content validation — are the column names, data types, and values in
  the file correct before it even hits the pipeline? Right now nothing checks 
  the file itself before Tidal picks it up.
                                                                                Data integrity — after the job runs, is the data in the DB actually correct?
   Did updates overwrite the right rows? Are there duplicates? Do the counts  
  between the source file and target table match exactly?
                                                                                Cross-file consistency — does every DRG in the exclusion file exist in the
  mapping table? If an exclusion references a DRG that doesn't have a mapping,
   the downstream pend/deny logic won't know what MDC to assign.
                                                                                Before I start writing TCs for these layers, I need to understand what
  validation is already built into the stored procedures and SSIS packages. If
   the SPs already reject bad column types, duplicate keys, and missing
  required fields, then my TCs just verify that works end-to-end with real      files in DEV. If they don't, then my TCs are the only validation and I need
  significantly more of them. That's the difference between writing around 11 
  new TCs and closer to 35. Can I get access to review the SP logic and SSIS
  packages so I can map what's already covered?

  I also have a few things I need clarity on. 
                                          
  On the exclusion file stories, I sent a message about 590587 having detailed
   ACs while 590589 is just high-level bullets. Are those supposed to match?    That determines whether QST needs additional test cases.
                                                                                On SIT vs UAT, the repo has separate folders with different test cases
  written in different styles. I want to make sure I understand the flow. Who 
  is responsible for SIT execution vs UAT? Am I owning one or both? And what's   the handoff process between them?                                             
  On environment access, I'll need VPN, S: drive, SSMS, and Tidal access to   
  start executing. What's the process to get that set up?
  
  Appreciate any answers you can get back to me before standup. Happy to walk   through any of this in more detail at 1:30.
                                                                                Thanks                                            

  Hi team,

  I've been getting up to speed on the test plan and wanted to share some thoughts and get  
  your input on a few things before standup.

  I went through the test repo to familiarize myself with what we have — 19 test cases      
  across SIT and UAT covering the file processing flow. Good coverage on the mapping file   
  side. I had a question on the exclusion file though — it looks like there are some        
  scenarios we might want to add, like file not found, access denied, and the
  update/terminate actions. I can put together a list if that would be helpful.

  One thing I was thinking about as I went through everything — our current test cases do a 
  solid job answering "did the pipeline work?" I was wondering if we should also be thinking
   about a couple of other angles:

  Are we validating the file content itself before it enters the pipeline? Things like      
  column names, data types, value ranges. Might be worth considering if Tidal picks up a bad
   file and it gets through.

  After the job runs, are we checking the actual data in the DB? Like confirming that       
  updates changed the right rows, business keys are unique, row counts match the source     
  file.

  And on the cross-file side — should we verify that every DRG in an exclusion file has a   
  corresponding mapping? Just thinking about what could happen downstream if one doesn't.   

  That said, I don't want to duplicate work that's already handled elsewhere. Do the stored 
  procedures or SSIS packages already validate some of this? If so, that changes the scope  
  quite a bit. Would it be possible for me to review the SP logic so I can see what's       
  already covered before proposing new test cases?

  A couple of other things I wanted to get clarity on:

  On the exclusion file stories — 590587 has really detailed ACs but 590589 is more high    
  level. Was curious if those are meant to align or if there's a reason they're different.  
  Just want to make sure I'm working off the right baseline.

  On SIT and UAT — I noticed the repo has both with different test case styles. I wanted to 
  make sure I understand the flow and who owns what so I can focus my efforts in the right  
  place.

  And on access — I'll need VPN, S: drive, SSMS, and Tidal to start executing. Happy to get 
  that process started whenever makes sense.

  Let me know your thoughts on any of this. Looking forward to discussing at 1:30.

  Thanks
-----
-----
  Email 1 — To: Manager | CC: Test Lead

  Hi [Manager],

  I've been getting up to speed on the test plan and wanted to share where I'm at and get   
  some direction on a few things.

  I went through the test repo to familiarize myself with our coverage — 19 test cases      
  across SIT and UAT covering the file processing flow. Good foundation on the mapping file 
  side. I noticed some areas on the exclusion file where we might want to add coverage, like
   file not found, access denied, and the update/terminate scenarios. I can put together a  
  detailed list if that would be helpful.

  As I was going through everything, I was thinking about whether we should also be
  considering some additional testing angles beyond file processing. Things like validating 
  file content before it hits the pipeline, verifying data integrity in the DB after jobs   
  run, and checking cross-file consistency between the mapping and exclusion files. I'd like
   to discuss whether these make sense for our scope.

  A few things I need clarity on to focus my efforts:

  On SIT and UAT — the repo has both with different test case styles. I want to make sure I 
  understand who owns what and what the handoff looks like so I'm working in the right area.

  On the exclusion file stories — 590587 has detailed ACs but 590589 is more high level. I  
  want to confirm whether those should align before I start writing test cases against them.

  On access — I'll need VPN, S: drive, SSMS, and Tidal access to start executing. Happy to  
  get that process started whenever makes sense.

  Looking forward to discussing at standup.

  Thanks

  ---
  Email 2 — To: Dev team | CC: Manager, Test Lead

  Hi team,

  I'm ramping up on testing for the file load pipeline and had a couple of technical        
  questions before I start writing additional test cases.

  I was looking at our test coverage and thinking about what validation is already built    
  into the stored procedures and SSIS packages. Before I propose new test cases for things  
  like column validation, data types, duplicate keys, and value ranges, I want to make sure 
  I'm not duplicating work that's already handled in the code. Would it be possible for me  
  to review the SP logic and SSIS packages so I can see what's already covered?

  Specifically wondering:

  What does the SP check for during the load process? Column types, required fields,        
  duplicates, ranges?

  Does the SSIS package reject anything before data reaches the SP? Like bad column names or
   wrong file structure?

  Is there any dev unit test coverage I could look at to understand what's already
  validated?

  Just want to be smart about where I focus the testing effort. No point writing 35 test    
  cases if the code already handles half of it.

  Also — on the exclusion file ACs, I sent a message earlier about 590587 vs 590589. Any    
  chance someone can confirm whether those should match?

  Appreciate any answers you can get back before standup at 1:30.

  Thanks
  
  
