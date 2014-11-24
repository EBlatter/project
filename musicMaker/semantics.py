#Import the library
from midiutil.MidiFile import MIDIFile

class MusicSemantics:

	def __init__(self, trackName = 'MusicMakerSong'):
		self.trackName = trackName
		# Create the MIDIFile Object with 1 track
		self.file = MIDIFile(1)

		# Tracks are numbered from zero. Times are measured in beats.
		self.track = 0
		self.time = 0

		# Add track name and tempo.
		self.file.addTrackName(self.track,self.time,trackName)
		self.file.addTempo(self.track,self.time,240)

		#start pitch and volume that everything else will be relative to
		self.pitch = 70
		self.maxVol = 0

	
	def addNote(self, note):
		# Add a note. addNote expects the following information:
		track = 0
		channel = 0
		pitch = self.pitch - int(note.pitch)
		duration = 1
		volume = 100.0*(float(note.volume)/self.maxVol)
		print 'volume', volume

		# Now add the note.
		self.file.addNote(track,channel,pitch,self.time,duration,volume)

		self.time += duration


	def findMaxVolume(self, notes):
		for note in notes:
			if float(note.volume) > self.maxVol:
				self.maxVol = float(note.volume)
		print self.maxVol

	def createSong(self, notes):
		self.findMaxVolume(notes)
		for note in notes:
			self.addNote(note)

		# And write it to disk.
		binfile = open(self.trackName+'.mid', 'wb')
		self.file.writeFile(binfile)

		binfile.close()