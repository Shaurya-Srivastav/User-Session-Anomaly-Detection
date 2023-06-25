data = [
     {
      "user": "user1",
      "timestamp": 1624518000,
      "source_ip": "192.168.0.100",
      "protocol": "NTLM"
    },
    {
      "user": "user2",
      "timestamp": 1624518100,
      "source_ip": "192.168.0.101",
      "protocol": "NTLM"
    },
    {
      "user": "user1",
      "timestamp": 1624518200,
      "source_ip": "192.168.0.102",
      "protocol": "NTLM"
    },
    {
      "user": "user3",
      "timestamp": 1624518300,
      "source_ip": "192.168.0.103",
      "protocol": "Kerberos"
    },
    {
      "user": "user1",
      "timestamp": 1624518400,
      "source_ip": "192.168.0.100",
      "protocol": "NTLM"
    },
    {
      "user": "user2",
      "timestamp": 1624518500,
      "source_ip": "192.168.0.105",
      "protocol": "NTLM"
    },
    {
      "user": "user3",
      "timestamp": 1624518600,
      "source_ip": "192.168.0.106",
      "protocol": "NTLM"
    },
    {
      "user": "user4",
      "timestamp": 1624518700,
      "source_ip": "192.168.0.107",
      "protocol": "NTLM"
    },
    {
      "user": "user2",
      "timestamp": 1624518800,
      "source_ip": "192.168.0.108",
      "protocol": "NTLM"
    },
    {
      "user": "user5",
      "timestamp": 1624518900,
      "source_ip": "192.168.0.109",
      "protocol": "Kerberos"
    },
    {
      "user": "user4",
      "timestamp": 1624519000,
      "source_ip": "192.168.0.110",
      "protocol": "NTLM"
    },
    {
      "user": "user5",
      "timestamp": 1624519100,
      "source_ip": "192.168.0.111",
      "protocol": "NTLM"
    },
    {
      "user": "user6",
      "timestamp": 1624519200,
      "source_ip": "192.168.0.112",
      "protocol": "NTLM"
    },
    {
      "user": "user3",
      "timestamp": 1624519300,
      "source_ip": "192.168.0.103",
      "protocol": "Kerberos"
    },
    {
      "user": "user5",
      "timestamp": 1624519400,
      "source_ip": "192.168.0.114",
      "protocol": "NTLM"
    },
    {
      "user": "user6",
      "timestamp": 1624519500,
      "source_ip": "192.168.0.115",
      "protocol": "NTLM"
    },
    {
      "user": "user7",
      "timestamp": 1624519600,
      "source_ip": "192.168.0.116",
      "protocol": "NTLM"
    },
    {
      "user": "user8",
      "timestamp": 1624519700,
      "source_ip": "192.168.0.117",
      "protocol": "NTLM"
    },
    {
      "user": "user9",
      "timestamp": 1624519800,
      "source_ip": "192.168.0.118",
      "protocol": "NTLM"
    },
    {
      "user": "user10",
      "timestamp": 1624519900,
      "source_ip": "192.168.0.119",
      "protocol": "Kerberos"
    },
    {
      "user": "user4",
      "timestamp": 1624520000,
      "source_ip": "192.168.0.110",
      "protocol": "NTLM"
    },
    {
      "user": "user5",
      "timestamp": 1624520100,
      "source_ip": "192.168.0.121",
      "protocol": "NTLM"
    }
]

# Create a dictionary to store the user sessions
user_sessions = {}

# Iterate over the data and analyze the sessions
for entry in data:
    user = entry["user"]
    source_ip = entry["source_ip"]
    protocol = entry["protocol"]

    # Check if the user already has a previous session
    if user in user_sessions:
        previous_session = user_sessions[user]
        previous_source_ip = previous_session["source_ip"]
        previous_protocol = previous_session["protocol"]

        # Compare the current session with the previous session
        if source_ip != previous_source_ip and protocol == previous_protocol:
            print(f"Anomaly detected for user {user}:")
            print(f"Previous session: source_ip={previous_source_ip}, protocol={previous_protocol}")
            print(f"Current session: source_ip={source_ip}, protocol={protocol}")
            print()

    # Update the user session with the current entry
    user_sessions[user] = {
        "source_ip": source_ip,
        "protocol": protocol
    }