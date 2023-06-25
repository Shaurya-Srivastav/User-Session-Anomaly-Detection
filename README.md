# User Session Anomaly Detection

This script analyzes user sessions and detects anomalies based on the source IP address and protocol. It compares each user's current session with their previous session and identifies any deviations.

## How it Works

The script uses a dictionary called `user_sessions` to store the current session information for each user. It iterates over the `data` list, which contains the user session data, and performs the following steps for each session:

1. Extract the user, source IP address, and protocol from the session entry.
2. Check if the user already has a previous session stored in the `user_sessions` dictionary.
3. If the user has a previous session, retrieve the source IP address and protocol of the previous session.
4. Compare the current session's source IP address with the previous session's source IP address and the current session's protocol with the previous session's protocol.
5. If the source IP addresses are different, and the protocols are the same, an anomaly is detected.
6. Print the details of the anomaly, including the user, previous session's source IP address and protocol, and the current session's source IP address and protocol.
7. Update the `user_sessions` dictionary with the current session information, replacing the previous session entry for the user.

The script continues to analyze each session in the `data` list, identifying anomalies whenever they occur. By comparing each session with the user's previous session, the script can detect any unexpected changes in the source IP address while the protocol remains the same.

## Algorithm

The algorithm used in this script follows a simple logic to detect anomalies in user sessions. Here's an overview of the algorithm:

1. Initialize an empty dictionary, `user_sessions`, to store the current session information for each user.
2. Iterate over each session in the `data` list.
3. For each session, extract the user, source IP address, and protocol.
4. Check if the user has a previous session stored in the `user_sessions` dictionary.
5. If the user has a previous session, compare the current session's source IP address with the previous session's source IP address and the current session's protocol with the previous session's protocol.
6. If the source IP addresses are different, and the protocols are the same, an anomaly is detected.
7. Print the details of the anomaly.
8. Update the `user_sessions` dictionary with the current session information.
9. Continue iterating over the remaining sessions.
10. Once all sessions have been analyzed, the script completes.

This algorithm efficiently compares each session with the previous session of the same user, allowing the script to identify anomalies and print their details.

## Usage

To use this script, follow these steps:

1. Make sure you have Python installed on your machine.
2. Clone this repository.
3. Open the terminal and navigate to the repository's directory.
4. Run the script using the command `python session_anomaly_detection.py`.
5. The script will output any detected anomalies for each user.

## Dependencies

This script does not have any external dependencies. It uses only the standard libraries available in Python.

## Data

The `data` variable in the script contains a sample dataset of user sessions. You can replace it with your own data for analysis. Each session is represented as a dictionary with the following attributes:

- `user`: The username of the user.
- `timestamp`: The timestamp of the session.
- `source_ip`: The source IP address of the session.
- `protocol`: The protocol used in the session.

```python
data = [
    {
        "user": "user1",
        "timestamp": 1624518000,
        "source_ip": "192.168.0.100",
        "protocol": "NT

LM"
    },
    {
        "user": "user2",
        "timestamp": 1624518100,
        "source_ip": "192.168.0.101",
        "protocol": "NTLM"
    },
    ...
]
```

## Output

The script iterates over the data and detects any anomalies in the user sessions. An anomaly is identified if the source IP address changes while the protocol remains the same for consecutive sessions of the same user.

The detected anomalies are printed to the console in the following format:

```
Anomaly detected for user {user}:
Previous session: source_ip={previous_source_ip}, protocol={previous_protocol}
Current session: source_ip={current_source_ip}, protocol={current_protocol}
```
