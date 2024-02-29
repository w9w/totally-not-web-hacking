### Exfiltration of parameters from GET
`(?<=\?|&)([a-zA-Z0-9_]+)`

### Exfiltration of parameters from POST application/json
"`([a-zA-Z_]+)":`

### Exfiltration of parameters from POST application/x-www-form-urlencoded
`([a-zA-Z_]+)=`

### All in one
(?<=\?|&)([a-zA-Z0-9_]+)|"([a-zA-Z_]+)":|([a-zA-Z_]+)=
