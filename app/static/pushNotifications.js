$(function () {
    var since = 0;
    setInterval(function () {
        $.ajax('/notifications?since=' + since).done(
            function (notifications) {
                for (var i = 0; i < notifications.length; i++) {
                    if (notifications[i].name === 'unread_message_count')
                        setMessageCount(notifications[i].data);
                    since = notifications[i].timestamp;
                }
            }
        );
    }, 10000);
});
