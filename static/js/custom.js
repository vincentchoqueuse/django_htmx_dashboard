document.addEventListener('DOMContentLoaded', function () {
    const modal = new bootstrap.Modal(document.getElementById("modal"))

    htmx.on("htmx:afterSwap", (e) => {
      if (e.detail.target.id == "modal-content") {
        modal.show()
      }
    });

    htmx.on("hidden.bs.modal", () => { 
        document.getElementById("modal-content").innerHTML = "";
        });

    htmx.on("htmx:afterRequest", (e) => {
      if (e.detail.xhr.status === 204) {
        modal.hide()
        document.getElementById("modal-content").innerHTML = "" }
      });
});