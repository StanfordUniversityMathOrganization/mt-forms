import math

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def signupsheets():
    start = 1
    end = 99
    team_size = 8
    event_name = "Stanford Math Tournament"

    id_len = int(math.floor(math.log10(end)+1))
    id_seq = [str(n).zfill(id_len) for n in range(start, end+1)]
    letter_seq = [chr(ord("A") - 1 + i) for i in range(1, team_size+1)]
    return render_template("signupsheets.html",
        event_name=event_name, id_seq=id_seq, letter_seq=letter_seq, last_letter=letter_seq[-1])

if __name__ == '__main__':
    app.run(debug=True)
