from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'music.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    songs = conn.execute('SELECT * FROM songs').fetchall()
    conn.close()
    return render_template('index.html', songs=songs)

@app.route('/play/<int:song_id>')
def play(song_id):
    conn = get_db_connection()
    song = conn.execute(
        'SELECT * FROM songs WHERE id = ?', (song_id,)
    ).fetchone()
    conn.close()
    return render_template('player.html', song=song)
@app.route('/add', methods=['GET', 'POST'])
def add_song():
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        file_path = request.form['file']

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO songs (title, artist, file_path) VALUES (?, ?, ?)',
            (title, artist, file_path)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('add_song.html')


if __name__ == '__main__':
    app.run(debug=True)