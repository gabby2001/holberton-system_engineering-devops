## Postmortem  

### Issue Summary:
On May 23th, 2018 at 1pm PST, the monitoring system reported a increased number of 500 server error. After diagnosis, the root cause was the server hard disk ran out of space and the server wasn’t working anymore. After adding a new disk and restarting the server, and the server was back to normal at 4pm PST.  
  
### Timeline:
1pm - The monitoring system reported 500 errors on the server
1:30pm-2:30pm - Started investigation, checked server hardware and software status reports  
2:30pm - Determined the server error was due to server storage reached limit
3pm-4pm - Installed a new hard disk drive and restarted server
4pm - server back to normal 
   
### Root Cause:
The server hard disk drive ran out of space.
   
### Future Prevention:
We will install a new monitoring tool that will send alert when storage space reaches capacity, so we can take needed action in advance.
