document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('a[href$=".pptx"]').forEach(function(link) {
    var href = link.getAttribute('href');
    var absoluteUrl = new URL(href, window.location.origin + window.location.pathname).href;
    var viewerUrl = 'https://view.officeapps.live.com/op/view.aspx?src=' + encodeURIComponent(absoluteUrl);
    link.setAttribute('href', viewerUrl);
    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'noopener');
  });
});
