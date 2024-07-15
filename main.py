import re

malicious_patterns = {
    r'FileInstall, .*': 'File installation from external source',
    r'Run, "?.*\.exe"?': 'Execution of executable file',
    r'RegWrite, .*': 'Registry modification',
    r'pwhr := COM_CreateObject\("WinHttp\.WinHttpRequest\.5\.1"\)': 'HTTP request creation',
    r'RunAsAdmin\(\)': 'Attempted privilege escalation',
    r'download_file_nofreeze\(.+\)': 'File download',
    r'sonlandir\(".+"\)': 'Process termination',
    r'simge_arguman_degis\(.+, .+\)': 'Shortcut modification',
    r'DllCall\("LoadLibrary", "Str", ".+"\)': 'Dynamic library loading',
    r'Run, sc stop .*': 'Service stop command',
    r'Run, sc delete .*': 'Service deletion command',
    r'COM_GetDefaultEvents': 'Access to COM events',
    r'COM_GetGuidOfName': 'GUID retrieval from name',
    r'COM_GetTypeInfoOfGuid': 'Type information retrieval for GUID',
    r'COM_ConnectObject': 'Connection establishment to COM object',
    r'COM_ScriptControl': 'Script execution control',
    r'RegExMatch\(.*, ".*"\)': 'Regular expression usage with dynamic pattern',
    r'SetTimer, .+, \d+': 'SetTimer function with numeric timer interval',
    r'SetTimer, .+, \w+': 'SetTimer function with variable timer interval',
    r'Hotkey, .+, .+': 'Hotkey registration with parameters',
    r'Scripting.Dictionary': 'Scripting.Dictionary object usage',
    r'FileOpen, .+, W': 'FileOpen with write mode',
    r'FileOpen, .+, R': 'FileOpen with read mode',
    r'FileOpen, .+, A': 'FileOpen with append mode',
    r'Send, .+': 'Direct keyboard input (Send command)',
    r'MouseMove, .+': 'Mouse movement control',
    r'Sleep, .+': 'Script pause (Sleep command)',
    r'Critical, .+': 'Critical section for interrupt prevention',
    r'WinActivate, .+': 'Window activation',
    r'WinWaitActive, .+': 'Waiting for window activation',
    r'Process, .+': 'Process manipulation (Process command)',
    r'FileAppend, .+': 'Appending to file (FileAppend command)',
    r'IfWinActive, .+': 'Conditional window activation',
    r'SetFormat, .+': 'SetFormat function for variable formatting',
    r'VarSetCapacity, .+': 'Memory allocation with VarSetCapacity',
    r'DetectHiddenWindows, .+': 'DetectHiddenWindows function call',
    r'ControlSend, .+': 'Sending control-specific messages (ControlSend command)',
    r'ControlClick, .+': 'Simulating control clicks (ControlClick command)',
    r'ImageSearch, .+': 'ImageSearch function call for image recognition',
    r'MouseClick, .+': 'Simulating mouse clicks (MouseClick command)',
    r'MouseGetPos, .+': 'Retrieving mouse position (MouseGetPos command)',
    r'WinWait, .+': 'Waiting for window existence (WinWait command)',
    r'WinWaitClose, .+': 'Waiting for window closure (WinWaitClose command)',
    r'WinClose, .+': 'Force-closing a window (WinClose command)',
    r'SetEnv, .+': 'Setting environment variables (SetEnv command)',
    r'EnvGet, .+': 'Retrieving environment variables (EnvGet command)',
    r'Loop, .+': 'Looping control (Loop command)',
    r'Click, .+': 'Mouse or keyboard click (Click command)',
    r'ControlGet, .+': 'Retrieving control-specific information (ControlGet command)',
    r'ControlMove, .+': 'Moving controls (ControlMove command)',
    r'ControlGetText, .+': 'Retrieving control text (ControlGetText command)',
    r'ControlSetText, .+': 'Setting control text (ControlSetText command)',
    r'ControlFocus, .+': 'Setting focus on a control (ControlFocus command)',
    r'ControlGetFocus, .+': 'Retrieving focused control (ControlGetFocus command)',
    r'ControlGetPos, .+': 'Retrieving control position (ControlGetPos command)',
    r'ControlGetList, .+': 'Retrieving control list (ControlGetList command)',
    r'ControlSendRaw, .+': 'Sending raw control messages (ControlSendRaw command)',
    r'ControlSendEvent, .+': 'Sending control events (ControlSendEvent command)',
    r'ControlSendText, .+': 'Sending text to a control (ControlSendText command)',
    r'ControlClick, .+': 'Simulating control clicks (ControlClick command)',
    r'ControlFocus, .+': 'Setting focus on a control (ControlFocus command)',
    r'ControlGetFocus, .+': 'Retrieving focused control (ControlGetFocus command)',
    r'ControlGetPos, .+': 'Retrieving control position (ControlGetPos command)',
    r'ControlGetList, .+': 'Retrieving control list (ControlGetList command)',
    r'ControlSendRaw, .+': 'Sending raw control messages (ControlSendRaw command)',
    r'ControlSendEvent, .+': 'Sending control events (ControlSendEvent command)',
    r'ControlSendText, .+': 'Sending text to a control (ControlSendText command)',
    r'ControlFocus, .+': 'Setting focus on a control (ControlFocus command)',
    r'ControlGetFocus, .+': 'Retrieving focused control (ControlGetFocus command)',
    r'ControlGetPos, .+': 'Retrieving control position (ControlGetPos command)',
    r'ControlGetList, .+': 'Retrieving control list (ControlGetList command)',
    r'ControlSendRaw, .+': 'Sending raw control messages (ControlSendRaw command)',
    r'ControlSendEvent, .+': 'Sending control events (ControlSendEvent command)',
    r'ControlSendText, .+': 'Sending text to a control (ControlSendText command)',
}

def check_for_malicious_code(script_text):
    for pattern, description in malicious_patterns.items():
        if re.search(pattern, script_text):
            print(f"Detected malicious pattern: {description}")
            return True
    return False

if __name__ == "__main__":
    with open('malicious_code.txt', 'r') as file:
        script_content = file.read()
    
    if check_for_malicious_code(script_content):
        print("The script contains malicious patterns.")
    else:
        print("No malicious patterns found.")
