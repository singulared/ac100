import xchat

__module_name__ = "ac100 flashlight" 
__module_version__ = "1.0" 
__module_description__ = "Add flashlight (side leds) for new messages. Work on Toshiba ac100 (paz00) platform." 

fl_contexts = []

def set_flashlight(hl_type=1):
    sys_fs = open('/sys/class/leds/nvec-led/brightness','w')
    sys_fs.write(str(hl_type))
    sys_fs.close()

def fl_hook(word, word_eol, userdata):
    if xchat.get_info('win_status') == 'active':
        return xchat.EAT_NONE
    set_flashlight(1)
    global fl_contexts
    context = xchat.get_context()
    if context not in fl_contexts:
        fl_contexts.append(xchat.get_context())
    return xchat.EAT_NONE
    
def focus_hook(word, word_eol, userdata):
    context = xchat.get_context()
    global fl_contexts
    if context in fl_contexts:
        fl_contexts.remove(context)
    if not len(fl_contexts):
        set_flashlight(0)
    return xchat.EAT_NONE    

xchat.hook_print("Focus Tab", focus_hook)
xchat.hook_print("Focus Window", focus_hook)
xchat.hook_print("Channel Action Hilight", fl_hook)
xchat.hook_print("Channel Msg Hilight", fl_hook)
