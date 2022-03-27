function setMessageCount(n) {
    let count = $('#message_count')
    count.text(n);
    count.css('visibility', n ? 'visible' : 'hidden');
}
