import random as rand
import pandas_test as pt
import smooth
from inception_include import *


def inception_phase_20_0(sm, num):

    mode = 0;
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
    onset_2 = 0.25

    
    
    # mode == 0 :
    chord_1 = C3
    chord_2 = G3
    chord_3 = A2
    chord_4 = E3
    chord_5 = F3
    chord_6 = C3
    chord_7 = D3
    chord_8 = G3
    chord_8_c = C3
    chord_1_b = F3
    chord_2_b = G3
    chord_3_b = C3
    chord_4_b = C3
    chord_5_b = D3
    chord_6_b = D3
    chord_7_b = E3
    chord_8_b = E3
        
    chorus_b_1 = F_major_bass
    chorus_b_2 = G_major_bass
    chorus_b_3 = C_major_bass
    chorus_b_4 = C_major_bass
    chorus_b_5 = D_minor_bass
    chorus_b_6 = D_minor_bass
    chorus_b_7 = E_major_bass
    chorus_b_8 = E_major_bass
        
    chorus_c_1 = C_major_bass
    chorus_c_2 = G_major_bass
    chorus_c_3 = A_minor_bass
    chorus_c_4 = E_minor_bass
    chorus_c_5 = F_major_bass
    chorus_c_6 = C_major_bass
    chorus_c_7 = D_minor_bass
    chorus_c_8 = G_major_bass
    chorus_c_8_c = C_major_bass
        
    scale_1 = C_major
    scale_2 = G_major
    scale_3 = A_minor
    scale_4 = E_minor
    scale_5 = F_major
    scale_6 = C_major
    scale_7 = D_minor
    scale_8 = G_major
    scale_8_c = C_major
    scale_1_b = F_major
    scale_2_b = G_major
    scale_3_b = C_major
    scale_4_b = C_major
    scale_5_b = D_minor
    scale_6_b = D_minor
    scale_7_b = E_major
    scale_8_b = E_major
    tone = 'major'
    tick_mode = tick_0
    beat = beat_0
    onset_mode = onset_0
    


    tick = 0
    note = 72;
    note_last = 72
    sm_th = 9

# AB
    while (tick < 6400):
        tick_round = tick%6400
        if tick_round < 800:
            chord = chord_1
            scale = scale_1
        elif 800 <= tick_round < 1600:
            chord = chord_2
            scale = scale_2
        elif 1600 <= tick_round < 2400:
            chord = chord_3
            scale = scale_3
        elif 2400 <= tick_round < 3200:
            chord = chord_4
            scale = scale_4
        elif 3200 <= tick_round < 4000:
            chord = chord_5
            scale = scale_5
        elif 4000 <= tick_round < 4800:
            chord = chord_6
            scale = scale_6
        elif 4800 <= tick_round < 5600:
            chord = chord_7
            scale = scale_7
        elif 5600 <= tick_round < 6400:
            chord = chord_8
            scale = scale_8
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(100,chord))
        note = pt.gen_next_note(scale[0],mode)
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(0,note))
        
        onset = rand.random()
        if onset > 0.3:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        
        note = pt.gen_next_note(note,mode)
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last =  note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        
        onset = rand.random()
        if onset > 0.4:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        tick = tick + 400
    
    
    note_last = 72
    sm_th = 9
    tick = 0
    # bridge
    while (tick < 6400):
        tick_round = tick%6400
        if tick_round < 800:
            chord = chord_1_b
            scale = scale_1_b
        elif 800 <= tick_round < 1600:
            chord = chord_2_b
            scale = scale_2_b
        elif 1600 <= tick_round < 2400:
            chord = chord_3_b
            scale = scale_3_b
        elif 2400 <= tick_round < 3200:
            chord = chord_4_b
            scale = scale_4_b
        elif 3200 <= tick_round < 4000:
            chord = chord_5_b
            scale = scale_5_b
        elif 4000 <= tick_round < 4800:
            chord = chord_6_b
            scale = scale_6_b
        elif 4800 <= tick_round < 5600:
            chord = chord_7_b
            scale = scale_7_b
        elif 5600 <= tick_round < 6400:
            chord = chord_8_b
            scale = scale_8_b
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(100,chord))
        note = pt.gen_next_note(scale[0],mode)
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(0,note))
        
        onset = rand.random()
        if onset > 0.2:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        
        note = pt.gen_next_note(note,mode)
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        
        onset = rand.random()
        if onset > 0.2:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        tick = tick + 800
    
    
    note_last = 72
    sm_th = 9
    tick = 0
    # C
    while (tick < 6400):
        tick_round = tick%6400
        if tick_round < 800:
            chord = chord_1
            scale = scale_1
        elif 800 <= tick_round < 1600:
            chord = chord_2
            scale = scale_2
        elif 1600 <= tick_round < 2400:
            chord = chord_3
            scale = scale_3
        elif 2400 <= tick_round < 3200:
            chord = chord_4
            scale = scale_4
        elif 3200 <= tick_round < 4000:
            chord = chord_5
            scale = scale_5
        elif 4000 <= tick_round < 4800:
            chord = chord_6
            scale = scale_6
        elif 4800 <= tick_round < 5200:
            chord = chord_7
            scale = scale_7
        elif 5200 <= tick_round < 5600:
            chord = chord_8
            scale = scale_8
        elif 5600 <= tick_round < 6400:
            chord = chord_8_c
            scale = scale_8_c
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(100,chord))
        note = pt.gen_next_note(scale[0],mode)
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(0,note))
        
        onset = rand.random()
        if onset > 0.1:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        
        note = pt.gen_next_note(note,mode)
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        
        onset = rand.random()
        if onset > 0.2:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        tick = tick + 400
        
#end automatic composing
    fp.write("#end automatic composing\n\n")
    
    
    fp.write("    midi.EndOfTrackEvent(tick=1, data=[])]])\n\n\n")
    fp.write("    midi.write_midifile(\"inception_phase_11_{}_{}.mid\", hh_midi)".format(tone,num))

    fp.close()

    #midi_file = 'inception_phase_11_{}_0.mid'.format(tone)
    #midi_play.play_music(midi_file)


