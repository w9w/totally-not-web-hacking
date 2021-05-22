##Burp suite suggestions:

1) Ever wondered what happens if you launch 5000 race conditions threads? I did so, and the results are surprising:
If we consume this script https://github.com/w9w/totally-not-web-hacking/blob/master/turbo-intruder-scripts/default-race.py-but-with-params.txt to the turbo intruder, mark parameter insertion point, and click on launch; there will be a decent raise in RAM consumption by burp (I had ~1200%). When I launched an attack, every OS application started lagging heavily; at some time, I couldn't even use an apple native app for screenshots that I was thinking of using my phone's camera, and even music stopped playing. Since coolers started working with the loudness they never had, I started emergency shut down. If PC would have a heart, it could have a heart attack for sure 😅

The bug here is not that the turbo intruder consumed that much memory, although, despite the number of concurrent connections, it's enormous memory consumption. Even after the closing of the extension, the burp suite still had problems with RAM consumption. The reason for this, I think, is the bug that represents a lack of threads clearing if threads were not fully created and an extension was closed. It could impact RAM consumption during the entire burp suite session, I suppose.

2) Add the "Disable OOS traffic capture" button along with the "And URL Is in target scope" button to the Proxy's dropdown filter settings to not go to the settings on the right every time and search for these two buttons. I added FB to OOS, but I often need to click four buttons when I need to test it.

3) When we re-arrange burp tabs, the result is not saved, and after reload of the app, arranging is resetting.

4) When target defined as out-of-scope using "Target" tab and "don't send items to Proxy if OOS" and "Intercept client request rule And URL is in scope," a lot of OOS requests could flow to live proxy listener (Intercept tab of Proxy's tab) although they are strictly in OOS list!

5) Out-of-scope requests (with the above configurations) still flow to the "HTTP history" tab, not only to the live capturing. Although they could be deleted after a few seconds after appearing, they could cause pain when you are trying to click on the correct request you need.

6) At some point, after some requests were caught in the live proxy interception, the mouse pointer is moving to the search bar - it doesn't allow us to forward/drop requests using hotkeys - CMD+F/CMD+D on macOS by default. The problem exists on macOS.

7) When a user clicked on the "Send" button to the Repeater and scrolls down, after the request was executed, the cursor point will be reset to the beginning. It isn't enjoyable when you found a text, were ready to highlight it, and copy it, but you need to do this again because of reloading.

8) Payload type "Numbers" in the Intruder doesn't process "Sequential" numbers range correctly - if we specify 01 to 09 burp will interpret it as 1 to 9. However, 11 to 19 works perfectly.

9) Please add an ability to view, edit and add burp's native scan checks. We can use 3rd party extension for just adding checks for $60, although most built-in checks are the same as default burp suite checks. There is a free alternative, but it'd be super cool if it were built-in.

10) Please consider adding an ability to edit time by default for a refresh in burp collaborator. Every time, I change it to 1 instead of 60.

11) If possible, it'd be great to attach a particular burp collar address forever so we can open collaborator after program reloads and see all-time logs.

12) Bug - we can't change/add hotkeys on MacOS. - Fixed, thank you.

13) No hotkey implemented for quick search in the intruder/repeater/proxy history.

14) Please add an ability to suppress the "live editing" error in the Intruder by default. When I'm trying to write something, a window pops up, and the progress is lost. An error pops up even when "pause" was clicked.

15) Bug - If we select a number as a payload type in the intruder tab and enter "From," "To," and "Step" values too fast, payload count won't be sent; hence Intruder job could not be run. We should erase and enter values again.

16) Bug - burp http history doesn't hide some file types when they are OOS, for example, svg and png.

17) Bug - on macOS, windows that demand access to a particular part of the disk still appear after each update. Considering updates occur pretty often, it's not convenient.

18) It'd super valuable if you add an ability to edit resource pool in an audit scan - now, the only option to add a resource pool with a different value is to create a new one. I usually delete the old.

19) Please add an ability to search through all the files from the list in the Intruder (payload options) to choose the right file. I have dozens of files with different payloads and every time; I have to scroll slowly and search with eyes the suitable file. Implementation of such a feature would significantly boost UX.

20) Please add "Add from list" (Payload type: Simple list) for "Payload options" in the Intruder for multiple folders so that we would not place all the files with payloads into one folder and search through the entire big list. For example, the first folder represents payloads for vulnerabilities' fuzzing -  it's one list that should be drop-downed when we click on the "add from list 'fuzzing' "; the second folder represents passwords/logins/misc -  it's another list that should be drop-downed when we click on the "add from list 'brute-force' ".

21) I'd also be glad if you add an ability to choose a list from a different directory right in the intruder tab. As of now, we need to go to the Predefined Payload Lists, clicking "Select directory", search for the different directory, clicking "OK," and then return to the previous folder again if needed.

22) Please add CTRL+Z shortcut to revert changes in the editor. Now it doesn't work although CTRL+C/CTRL+A work fine.

23) Session handling rule for BS proxy traffic isn't working - scope All URLs, macOS.

24) Please add the possibility to detach particular extension tabs in the "Window" functionality at the top. Now, there is only a possibility to detach built-in windows like Sequencer and Decoder.

25) If possible, please consider adding the setting to detach windows by default so we won't detach particular windows after the program reload.
