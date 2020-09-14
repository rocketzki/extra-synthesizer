$("#btn-speak").click(() => {
    let backend_url = "http://localhost:8000/synthesizer/synthesize";
    console.log("elo")
    $.ajax({
        url: backend_url,
        method: "POST",
        data: {text: $('#synth-text-area').val(), ssml: $('#ssml').is(":checked"), enhanced: $('#enhanced').is(":checked")},
    }).done((data) => {
        let audio = new Audio();
        // audio.src = "data:audio/wave;" + data;
        audio.src = "data:audio/wave;base64," + data;

        audio.play();
        audio.onended = () => {
            alert("Ended playing first part");
        }
    })
});


$("#btn-clear").click(() => {
    $("#synth-text-area").val = ""
});
