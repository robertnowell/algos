/*
Prompt
Write a function that accepts an API response formatted as a JSON string. This function should parse, validate, and map the response JSON based on the following specifications.

Validation of the response should be checked using the value of Response.Status. If the Status value is not 'Success', then an error should be thrown. A reason string for the response failure can be found at Response.Reason and should be included with the thrown error's mesasge.

If the response is considered successful, map the result to the following object specification:

report: The base object containing the report
report.personal: A collection of personal information
report.personal.address: The most recent address of the consumer, taken from Response.Results[].Addresses[], where the most recent date is determined by the MoveInDate of Response.Results[].Addresses[]
report.personal.address.street: The combination of Street1 and Street2 of the most recent address of the consumer
report.personal.address.city: The city of the most recent address of the consumer
report.personal.address.state: The state of the most recent address of the consumer
report.personal.address.postalCode: The zip of the most recent address of the consumer
report.accounts[]: A list of accounts for the consumer, taken from Response.Results[].Accounts[]
report.accounts[].accountId: The id for the account
report.accounts[].balance: The current balance for the account, in a numeric format
report.accounts[].currency: The 3-digit ISO currency code for the account
report.accounts[].status: The current status for the account, mapped according to the given "Account Statuses" mappings below
report.summary: The summary for the report
report.summary.balance: The sum of all balances of all accounts
report.summary.openAccounts: The count of all accounts which have a mapped status of 'open'
Lookups
Response Statuses

Success
Failed
Account Status Mappings

Active -> open
Cancelled -> closed
Overdrawn -> open
*/
const exampleJson = `{
  "Response": {
    "Client": "Nova",
    "Version": "10.4.23",
    "Status": "Failed",
    "Reason": "failure",
    "Results": [
      {
        "Addresses": [
          {
            "MoveInDate": "2010-01-01",
            "Street1": "321 First Avenue",
            "Street2": "",
            "City": "Destination Town",
            "State": "CA",
            "Zip": "54321"
          },
          {
            "MoveInDate": "2011-04-23",
            "Street1": "123 Somewhere St",
            "Street2": "Apt 7A",
            "City": "Placeville",
            "State": "CA",
            "Zip": "12345"
          },
          {
            "MoveInDate": "Unknown",
            "Street1": "999 Other Road",
            "Street2": "",
            "City": "Upriver",
            "State": "CA",
            "Zip": "66666"
          },
          {
            "MoveInDate": "2012-08-03",
            "Street1": "123 Somewhere St",
            "Street2": "Apt 5B",
            "City": "Placeville",
            "State": "CA",
            "Zip": "12345"
          }
        ],
        "Accounts": [
          {
            "ID": "11111",
            "Currency": "USD",
            "Balance": "123.65",
            "Status": "Active"
          },
          {
            "ID": "22222",
            "Currency": "USD",
            "Balance": "0.0",
            "Status": "Cancelled"
          },
          {
            "ID": "33333",
            "Currency": "USD",
            "Balance": "-4.53",
            "Status": "Overdrawn"
          }
        ]
      }
    ]
  }
}`;
let SUCCESS = "Success";
let FAILED = "Failed";
let statuses = {
  "Active": "open",
  "Cancelled": "closed",
  "Overdrawn": "open",
};

let findMostRecentAddress = addresses => {
  let mostRecentDate = null;
  let mostRecentAddress = null;
  addresses.forEach(a => {
    let moveInDate = Date.parse(a.MoveInDate);

    if (mostRecentDate === null || mostRecentDate < moveInDate) {
      mostRecentDate = moveInDate;
      mostRecentAddress = a;
    }
  });
  return mostRecentAddress;
}

let parseAccounts = (accounts, summary) => {
  let res = accounts.map( a => {
    summary.balance += Number.parseFloat(a.Balance)
    let acct = {
      accountId: a.ID,
      balance: Number.parseFloat(a.Balance),
      currency: a.Currency,
      status: statuses[a.Status],
    }
    if (acct.status === "open"){
      summary.openAccounts++;
    }
    return acct;
  })
  return res;
}

let processJSON = s => {
  let summary = {
    "balance": 0,
    "openAccounts": 0,
  };

  let d = JSON.parse(s);
  console.log(d.Response.Results);
  if (d.Response.Status === FAILED){
    throw new Error(d.Response.Reason);
  }

  let mostRecentAddress = findMostRecentAddress(d.Response.Results[0].Addresses);
  console.log(mostRecentAddress);

  let result = {};
  result.report = d;
  result.personal = {
    address: {
      street: mostRecentAddress.Street1 + " " + mostRecentAddress.Street2,
      city: mostRecentAddress.City,
      state: mostRecentAddress.State,
      postalCode: mostRecentAddress.Zip,
    }
  };
  result.accounts = parseAccounts(d.Response.Results[0].Accounts, summary);
  result.summary = summary;
  console.log(result);
}

processJSON(exampleJson);

/*
parse
  var obj = JSON.parse(string);

validate
  check status
    if not success, throw error with reason
  else
    return result of map
  
map
  
*/
