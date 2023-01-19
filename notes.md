# Summary of Findings
The main benefit discovered by the paper is that a GPT-like autoregressive decoder network can perform far better at synthesizing speech with natural sounding intonation than traditional approaches.

The use of a neural compressor replaces the use of mel spectrograms as an intermediate representation, and removes the need of a seperate neural vocoder. The benefit of using such an approach just means that the indermediate representation is far lower dimensional.

Question is, would the same results apply if we directly generated a mel spectrogram with the same transformer based architecture?
___
## Questions

What role does the compression network play in improving performance beyond efficiency? Is a temporally based prompt the best idea for representing our desired voices?

We knew that tranformer and attention-heavy methods tend to better capture small nuances in reconstruction better than a purely recurrent approach, why do previous attempts at transformer based TTS systems fall short? Is it just volume of training data?
___
## Experiment Plans
experiment with encodec, see how important the first quantizer is to reconstruction. What kind of information does it encode, is it equivalent to a low-fidelity representation of the audio. If so, are we effectivley just upsampling in the latent space?

If this is the case, then the normal logic holds that the first low-fidelity representation is the most important as intonation and general speech structure can all be perfectly represented there. Similar to generating a decent sample with a lower fidelity melspec and vocoder and then upsampling later as it is a seperate problem.

What do I add to this? How do I improve?

Need to find weak points of existing model before I tear into new ground.
___
## Ideas
Speaker embedding space approach makes no sense. It's a fluid representation, and as you add new speech data to define a speaker it essentially changes the defenition of that speaker. Would it be smart to truncate it regardless? Embedding models provide one vector of fixed length regardless of the amount of information that they receive as input. Valuble to create a 