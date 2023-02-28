 document.addEventListener('click', function (event) {

            if (!event.target.closest('#menu')) {
                closeSidebar();
                console.log("h");
            }
            else {
                console.log("he");
                expand();
            }

        });

        function closeSidebar() {
            const menu = document.getElementById("menu");
            menu.className = "side-bar";
        }

        function expand() {

            const menu = document.getElementById("menu")
            console.log(menu.className);
            if (menu.className == "side-bar-expand") {
                console.log("sup")
                menu.className = "side-bar"
            }
            else {
                menu.className = "side-bar-expand";
                console.log("heh")
            }
        }

