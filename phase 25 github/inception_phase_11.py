import random as rand
import pandas_test as pt
import smooth


def inception_phase_11(mode, sm, num):

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
    C3 = 48
    D3 = 50
    E3 = 52
    F3 = 53
    G3 = 55
    A2 = 45
    B2 = 47
    G2 = 43
    B3 = 59
    F2 = 41
    A3 = 57

    C5 = 72
    D5 = 74
    E5 = 76
    F5 = 77
    G5 = 79
    A5 = 81
    B5 = 83

    Gb5 = 78
    Gb3 = 54
    Ab5 = 80
    Ab3 = 56
    Bb3 = 58
    Bb5 = 82
    Eb3 = 51
    Eb5 = 75

    scale_C = [C5,D5,E5,F5,G5,A5,B5]
    C_major = [C5,E5,G5,E5]
    G_major = [G5,B5,D5,B5]
    A_minor = [A5,C5,E5,C5]
    E_minor = [E5,G5,B5,G5]
    F_major = [F5,A5,C5,A5]
    D_minor = [D5,F5,A5,F5]
    D_major = [D5,Gb5,A5,Gb5]
    E_major = [E5,Ab5,B5,Ab5]
    
    
    C_major_bass = [C3,E3,G3,E3]
    G_major_bass = [G2,B2,D3,B2]
    A_minor_bass = [A2,C3,E3,C3]
    E_minor_bass = [E3,G3,B3,G3]
    E_major_bass = [E3,Ab3,B3,Ab3]
    F_major_bass = [F2,A2,C3,A2]
    D_minor_bass = [D3,F3,A3,F3]
    D_major_bass = [D3,Gb3,A3,Gb3]
    E_major_bass = [E3,Ab3,B3,Ab3]
    
    C_major_7_bass = [C3,E3,G3,Bb3]
    F_major_7_bass = [F2,A2,C3,Eb3]
    G_major_7_bass = [G2,B2,D3,F3]
    
    tick_0 = 6400
    tick_1 = 6400
    tick_2 = 9600
    
    beat_0 = 100
    beat_1 = 100
    beat_2 = 200
    
    onset_0 = 0.1
    onset_1 = 0.1
    onset_2 = 0.25

    if mode == 1:
        chord_1 = A2
        chord_2 = D3
        chord_3 = G3
        chord_4 = C3
        chord_5 = D3
        chord_6 = A2
        chord_7 = F3
        chord_8 = E3
        chord_8_c = A2
        chord_1_b = G3
        chord_2_b = A2
        chord_3_b = G3
        chord_4_b = A2
        chord_5_b = F3
        chord_6_b = F3
        chord_7_b = E3
        chord_8_b = E3
        
        chorus_b_1 = G_major_bass
        chorus_b_2 = A_minor_bass
        chorus_b_3 = G_major_bass
        chorus_b_4 = A_minor_bass
        chorus_b_5 = F_major_bass
        chorus_b_6 = F_major_bass
        chorus_b_7 = E_major_bass
        chorus_b_8 = E_major_bass
        
        chorus_c_1 = A_minor_bass
        chorus_c_2 = D_minor_bass
        chorus_c_3 = G_major_bass
        chorus_c_4 = C_major_bass
        chorus_c_5 = D_minor_bass
        chorus_c_6 = A_minor_bass
        chorus_c_7 = F_major_bass
        chorus_c_8 = E_major_bass
        chorus_c_8_c = A_minor_bass
        
        scale_1 = A_minor
        scale_2 = D_minor
        scale_3 = G_major
        scale_4 = C_major
        scale_5 = D_minor
        scale_6 = A_minor
        scale_7 = F_major
        scale_8 = E_major
        scale_8_c = A_minor
        scale_1_b = G_major
        scale_2_b = A_minor
        scale_3_b = G_major
        scale_4_b = A_minor
        scale_5_b = F_major
        scale_6_b = F_major
        scale_7_b = E_major
        scale_8_b = E_major
        tone = 'minor'
        tick_mode = tick_1
        beat = beat_1
        onset_mode = onset_1
    
    elif mode == 0 :
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
    
    else:
        
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

    tick = 0
    note = 72;
    note_last = 72
    sm_th = 9

# AB
    while (tick < tick_mode):
        tick_round = tick%tick_mode
        if tick_round < 800:
            chord = chorus_c_1
            scale = scale_1
        elif 800 <= tick_round < 1600:
            chord = chorus_c_2
            scale = scale_2
        elif 1600 <= tick_round < 2400:
            chord = chorus_c_3
            scale = scale_3
        elif 2400 <= tick_round < 3200:
            chord = chorus_c_4
            scale = scale_4
        elif 3200 <= tick_round < 4000:
            chord = chorus_c_5
            scale = scale_5
        elif 4000 <= tick_round < 4800:
            chord = chorus_c_6
            scale = scale_6
        elif 4800 <= tick_round < 5600:
            chord = chorus_c_7
            scale = scale_7
        elif 5600 <= tick_round < 6400:
            chord = chorus_c_8
            scale = scale_8
        elif 6400 <= tick_round < 7200:
            chord = chorus_c_9
            scale = scale_9
        elif 7200 <= tick_round < 8000:
            chord = chorus_c_10
            scale = scale_10
        elif 8000 <= tick_round < 8800:
            chord = chorus_c_11
            scale = scale_11
        elif 8800 <= tick_round < 9600:
            chord = chorus_c_12
            scale = scale_12
        
        #1
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(beat/2,chord[0]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[1]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[2]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[3]))
        
        note = pt.gen_next_note(note,mode)
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
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))
        #4
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))
        #5
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))
    #6
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
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
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))
    #8
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))

        
        
        tick = tick + beat * 4


    #note_last = 72
    sm_th = 9
    tick = 0
# bridge
    while (tick < tick_mode):
        tick_round = tick%tick_mode
        if tick_round < 800:
            chord = chorus_b_1
            scale = scale_1_b
        elif 800 <= tick_round < 1600:
            chord = chorus_b_2
            scale = scale_2_b
        elif 1600 <= tick_round < 2400:
            chord = chorus_b_3
            scale = scale_3_b
        elif 2400 <= tick_round < 3200:
            chord = chorus_b_4
            scale = scale_4_b
        elif 3200 <= tick_round < 4000:
            chord = chorus_b_5
            scale = scale_5_b
        elif 4000 <= tick_round < 4800:
            chord = chorus_b_6
            scale = scale_6_b
        elif 4800 <= tick_round < 5600:
            chord = chorus_b_7
            scale = scale_7_b
        elif 5600 <= tick_round < 6400:
            chord = chorus_b_8
            scale = scale_8_b
        elif 6400 <= tick_round < 7200:
            chord = chorus_b_9
            scale = scale_9_b
        elif 7200 <= tick_round < 8000:
            chord = chorus_b_10
            scale = scale_10_b
        elif 8000 <= tick_round < 8800:
            chord = chorus_b_11
            scale = scale_11_b
        elif 8800 <= tick_round < 9600:
            chord = chorus_b_12
            scale = scale_12_b
    #1
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(beat/2,chord[0]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[1]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[2]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[3]))

        note = pt.gen_next_note(note,mode)
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
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))
    #4
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))
    #5
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))
    #6
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
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
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))
    #8
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(beat/2,note,v))

        tick = tick + beat * 4


    #note_last = 72
    sm_th = 9
    tick = 0 
# C
    while (tick < tick_mode):
        tick_round = tick%tick_mode
        if tick_round < 800:
            chord = chorus_c_1
            scale = scale_1
        elif 800 <= tick_round < 1600:
            chord = chorus_c_2
            scale = scale_2
        elif 1600 <= tick_round < 2400:
            chord = chorus_c_3
            scale = scale_3
        elif 2400 <= tick_round < 3200:
            chord = chorus_c_4
            scale = scale_4
        elif 3200 <= tick_round < 4000:
            chord = chorus_c_5
            scale = scale_5
        elif 4000 <= tick_round < 4800:
            chord = chorus_c_6
            scale = scale_6
        elif 4800 <= tick_round < 5200:
            chord = chorus_c_7
            scale = scale_7
        elif 5200 <= tick_round < 5600:
            chord = chorus_c_8
            scale = scale_8
        elif 5600 <= tick_round < 6400:
            chord = chorus_c_8_c
            scale = scale_8_c
        elif 6400 <= tick_round < 7200:
            chord = chorus_c_9
            scale = scale_9
        elif 7200 <= tick_round < 8000:
            chord = chorus_c_10
            scale = scale_10
        elif 8000 <= tick_round < 8800:
            chord = chorus_c_11
            scale = scale_11
        elif 8800 <= tick_round < 9600:
            hord = chorus_c_12
            scale = scale_12
     #1
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(beat/2,chord[0]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[1]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[2]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[3]))
        note = pt.gen_next_note(note,mode)
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
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(beat/2,chord[1]))
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

    #5
        onset = rand.random()
        if onset > onset_mode:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(beat/2,chord[2]))
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
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(beat/2,chord[3]))
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

        tick = tick + beat * 4
        
#end automatic composing
    fp.write("#end automatic composing\n\n")
    
    
    fp.write("    midi.EndOfTrackEvent(tick=1, data=[])]])\n\n\n")
    fp.write("    midi.write_midifile(\"inception_phase_11_{}_{}.mid\", hh_midi)".format(tone,num))

    fp.close()

    #midi_file = 'inception_phase_11_{}_0.mid'.format(tone)
    #midi_play.play_music(midi_file)


