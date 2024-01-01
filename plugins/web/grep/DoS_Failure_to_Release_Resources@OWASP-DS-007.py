"""
owtf is an OWASP+PTES-focused try to unite great tools and facilitate pen testing
Copyright (c) 2011, Abraham Aranguren <name.surname@gmail.com> Twitter: @7a_ http://7-a.org
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;

GREP Plugin for DoS Failure to Release Resources (OWASP-DS-007)
https://www.owasp.org/index.php/Testing_for_DoS_Failure_to_Release_Resources_%28OWASP-DS-007%29
NOTE: GREP plugins do NOT send traffic to the target and only grep the HTTP Transaction Log
"""

import string, re
import cgi

DESCRIPTION = "Searches transaction DB for timing information"

def run(Core, PluginInfo):
	#Core.Config.Show()
	NuTransactions = 10
	SlowTransactions = []
	Command, IDs = Core.DB.Transaction.GrepTopTransactionIDsBySpeed(NuTransactions, "Desc") # Get Top 10 slowest transactions
	for ID in IDs:
		if Transaction := Core.DB.Transaction.GetByID(ID): # Transaction Found in DB
			SlowTransactions.append(Transaction)
	Content = "<p>Top "+str(len(SlowTransactions))+" slowest transactions</p>"
	Content += "<p>Hint: You can also sort by time in descending order on the "+Core.Reporter.Render.DrawButtonLink('Transaction log', Core.Config.GetHTMLTransacLog(True))+"</p>"
	Content += Core.Reporter.DrawHTTPTransactionTable(SlowTransactions)
	Content += Core.Reporter.DrawCommandTable(Command) # Show command used to generate info
	return Content

