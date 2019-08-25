import random as rand
import pandas_test as pt
import smooth
from inception_include import *

def inception_phase_20_blue(sm, num):

    mode = 2;
    fp = open("auto_phase_11.py", "w")

#start composing MIDI
    fp.write("#Inception phase 11\n");
    fp.write("import midi\n\n\n")
    fp.write("def midi_gen():\n")
    fp.write("    hh_midi = midi.Pattern(tracks=[[midi.TimeSignatureEvent(tick=0, data=[4, 2, 24, 8]),")
    midi_setup = ["    midi.KeySignatureEvent(tick=0, data=[0, 0]),\n",
              "    midi.EndOfTrackEvent(tick=1, data=[])],\n",
              "    [midi.ControlChangeEvent(tick=0, channel=0, data=[91, 58]),\n",
              "    midi.ControlChangeEvent(tick=0, channel=0, data=[10, 69]),\n",
              "    midi.ControlChangeEvent(tick=0, channel=0, data=[0, 0]),\n",
              "    midi.ControlChangeEvent(tick=0, channel=0, data=[32, 0]),\n",
              "    midi.ProgramChangeEvent(tick=0, channel=0, data=[0]),\n\n"]
              
    midi_setup_2 = [ "    [midi.ControlChangeEvent(tick=0, channel=0, data=[91, 58]),\n",
                     "    midi.ControlChangeEvent(tick=0, channel=0, data=[10, 69]),\n",
                     "    midi.ControlChangeEvent(tick=0, channel=0, data=[0, 0]),\n",
                     "    midi.ControlChangeEvent(tick=0, channel=0, data=[32, 0]),\n",
                     "    midi.ProgramChangeEvent(tick=0, channel=1, data=[33]),\n\n"]

    fp.writelines(midi_setup)

#automatic composing
    fp.write("#automatic composing\n")
    
    
    
    tick_0 = 6400
    tick_1 = 6400
    tick_2 = 9600
    
    beat_0 = 100
    beat_1 = 100
    beat_2 = 200
    
    onset_0 = 0.1
    onset_1 = 0.1
    onset_2 = 0.5


        
    chorus_b_1 = C_major_7_bass
    chorus_b_2 = C_major_7_bass
    chorus_b_3 = C_major_7_bass
    chorus_b_4 = C_major_7_bass
    chorus_b_5 = F_major_7_bass
    chorus_b_6 = F_major_7_bass
    chorus_b_7 = C_major_7_bass
    chorus_b_8 = C_major_7_bass
    chorus_b_9 = G_major_7_bass
    chorus_b_10 = G_major_7_bass
    chorus_b_11 = C_major_7_bass
    chorus_b_12 = C_major_7_bass
        
    chorus_c_1 = C_major_7_bass
    chorus_c_2 = C_major_7_bass
    chorus_c_3 = C_major_7_bass
    chorus_c_4 = C_major_7_bass
    chorus_c_5 = F_major_7_bass
    chorus_c_6 = F_major_7_bass
    chorus_c_7 = C_major_7_bass
    chorus_c_8 = C_major_7_bass
    chorus_c_8_c = C_major_7_bass
    chorus_c_9 = G_major_7_bass
    chorus_c_10 = G_major_7_bass
    chorus_c_11 = C_major_7_bass
    chorus_c_12 = C_major_7_bass
        
    chorus_beat_1 = C_major_7
    chorus_beat_2 = C_major_7
    chorus_beat_3 = C_major_7
    chorus_beat_4 = C_major_7
    chorus_beat_5 = F_major_7
    chorus_beat_6 = F_major_7
    chorus_beat_7 = C_major_7
    chorus_beat_8 = C_major_7
    chorus_beat_9 = G_major_7
    chorus_beat_10 = G_major_7
    chorus_beat_11 = C_major_7
    chorus_beat_12 = C_major_7

    scale_1 = C_major
    scale_2 = C_major
    scale_3 = C_major
    scale_4 = C_major
    scale_5 = F_major
    scale_6 = F_major
    scale_7 = C_major
    scale_8 = C_major
    scale_8_c = C_major
    scale_9 = G_major
    scale_10 = G_major
    scale_11 = C_major
    scale_12 = C_major

    scale_1_b = C_major
    scale_2_b = C_major
    scale_3_b = C_major
    scale_4_b = C_major
    scale_5_b = F_major
    scale_6_b = F_major
    scale_7_b = C_major
    scale_8_b = C_major
    scale_9_b = G_major
    scale_10_b = G_major
    scale_11_b = C_major
    scale_12_b = C_major
        
    tone = 'blue'
    tick_mode = tick_2
    beat = beat_2
    onset_mode = onset_2

    note = 72;
    note_last = 72


    #note_last = 72
    sm_th = 9
    tick = 0
    bass_cnt = 0
    even = 0
# C
    while (tick < tick_mode):
        bass_cnt = 0
        tick_round = tick%tick_mode
        if tick_round < 800:
            chord = chorus_c_1
            scale = scale_1
            chorus_beat = chorus_beat_1
            even = 0
        elif 800 <= tick_round < 1600:
            chord = chorus_c_2
            scale = scale_2
            chorus_beat = chorus_beat_2
            even = 1
        elif 1600 <= tick_round < 2400:
            chord = chorus_c_3
            scale = scale_3
            chorus_beat = chorus_beat_3
            even = 0
        elif 2400 <= tick_round < 3200:
            chord = chorus_c_4
            scale = scale_4
            chorus_beat = chorus_beat_4
            even = 1
        elif 3200 <= tick_round < 4000:
            chord = chorus_c_5
            scale = scale_5
            chorus_beat = chorus_beat_5
            even = 0
        elif 4000 <= tick_round < 4800:
            chord = chorus_c_6
            scale = scale_6
            chorus_beat = chorus_beat_6
            even = 1
        elif 4800 <= tick_round < 5600:
            chord = chorus_c_7
            scale = scale_7
            chorus_beat = chorus_beat_7
            even = 0
        elif 5600 <= tick_round < 6400:
            chord = chorus_c_8
            scale = scale_8
            chorus_beat = chorus_beat_8
            even = 1
        elif 6400 <= tick_round < 7200:
            chord = chorus_c_9
            scale = scale_9
            chorus_beat = chorus_beat_9
            even = 0
        elif 7200 <= tick_round < 8000:
            chord = chorus_c_10
            scale = scale_10
            chorus_beat = chorus_beat_10
            even = 1
        elif 8000 <= tick_round < 8800:
            chord = chorus_c_11
            scale = scale_11
            chorus_beat = chorus_beat_11
            even = 0
        elif 8800 <= tick_round < 9600:
            hord = chorus_c_12
            scale = scale_12
            chorus_beat = chorus_beat_12
            even = 1
        
        if even == 0:
            bass_cnt = [0,1,2,3]
        else:
            bass_cnt = [4,3,2,1]
     #1
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(beat/2,chord[bass_cnt[0]]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 55]),\n".format(0,chorus_beat[0]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 55]),\n".format(0,chorus_beat[1]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 55]),\n".format(0,chorus_beat[2]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 55]),\n".format(0,chorus_beat[3]))
        note = pt.gen_next_note(scale[0],mode)
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(0,note))
     
     #2
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        
        #fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(beat/2,chord[1]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))
    #3
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{},0]),\n".format(beat/2,chord[bass_cnt[1]]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(0,note,v))
       
    #4
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note

        #fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(beat/2,chord[3]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))
        onset = rand.random()
        if onset > onset_mode:
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 65]),\n".format(0,chorus_beat[0]))
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 65]),\n".format(0,chorus_beat[1]))
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 65]),\n".format(0,chorus_beat[2]))
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 65]),\n".format(0,chorus_beat[3]))

    #5
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(beat/2,chord[bass_cnt[2]]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(0,note,v))

    #6
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        
        #fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(beat/2,chord[3]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))

    #7
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(beat/2,chord[bass_cnt[3]]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(0,note,v))
        
    #8
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        
        #fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(beat/2,chord[3]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))
        
        fp.write("# 4 beat\n")
        tick = tick + beat * 4

        

    fp.write("    midi.EndOfTrackEvent(tick=1, data=[])],\n\n\n")

    
    fp.write("#Bass line\n")
    
    tick = 0
    fp.writelines(midi_setup_2)
# Bass line
    while (tick < tick_mode):
        bass_cnt = 0
        tick_round = tick%tick_mode
        if tick_round < 800:
            chord = chorus_c_1
            even = 0
        elif 800 <= tick_round < 1600:
            chord = chorus_c_2
            even = 1
        elif 1600 <= tick_round < 2400:
            chord = chorus_c_3
            even = 0
        elif 2400 <= tick_round < 3200:
            chord = chorus_c_4
            even = 1
        elif 3200 <= tick_round < 4000:
            chord = chorus_c_5
            even = 0
        elif 4000 <= tick_round < 4800:
            chord = chorus_c_6
            even = 1
        elif 4800 <= tick_round < 5600:
            chord = chorus_c_7
            even = 0
        elif 5600 <= tick_round < 6400:
            chord = chorus_c_8
            even = 1
        elif 6400 <= tick_round < 7200:
            chord = chorus_c_9
            even = 0
        elif 7200 <= tick_round < 8000:
            chord = chorus_c_10
            even = 1
        elif 8000 <= tick_round < 8800:
            chord = chorus_c_11
            even = 0
        elif 8800 <= tick_round < 9600:
            chord = chorus_c_12
            even = 1

        if even == 0:
            bass_cnt = [0,1,2,3]
        else:
            bass_cnt = [4,3,2,1]
    #1
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 100]),\n".format(beat/2,chord[bass_cnt[0]]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(beat/2,chord[bass_cnt[2]]))
        

    #3

        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{},100]),\n".format(beat/2,chord[bass_cnt[1]]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{},0]),\n".format(beat/2,chord[bass_cnt[3]]))


    #5

        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 100]),\n".format(beat/2,chord[bass_cnt[2]]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(beat/2,chord[bass_cnt[1]]))

    #7

        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 100]),\n".format(beat/2,chord[bass_cnt[3]]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(beat/2,chord[bass_cnt[1]]))
        
    
        tick = tick + beat * 4




    
    
        
#end automatic composing
    fp.write("#end automatic composing\n\n")
    
    
    fp.write("    midi.EndOfTrackEvent(tick=1, data=[])]])\n\n\n")
    fp.write("    midi.write_midifile(\"inception_phase_11_{}_{}.mid\", hh_midi)".format(tone,num))

    fp.close()

    #midi_file = 'inception_phase_11_{}_0.mid'.format(tone)
    #midi_play.play_music(midi_file)


