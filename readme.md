Oxford Buildings Benchmark
==========================

This is a repository that contains a dump of the Oxford VGG building dataset
benchmark data, with the evaluation script.

This is more or less a vis-a-vis clone of the ground truth data, only published
to be open about any potential disputes as the benchmark script has changed.

Computing the average precision with Python
-------------------------------------------

 * `python compute_ap.py christ_church_1 rank_list.txt` for the first Christ Church query.

Computing the average precision with original C++ code
------------------------------------------------------

This is only provided as a baseline for comparison - we use the Python evaluation
script for all of the benchmark results we publish.

 * Compile the compute_ap.cpp file, using (on linux) `g++ -O compute_ap.cpp -o compute_ap`.
 * To compute the average precision for a ranked list, rank_list.txt, one runs `./compute_ap christ_church_1 rank_list.txt`, for the first Christ Church query, etc.

Acknowledgements
----------------

This data has been provided by the Oxford Visual Geometry Group.

_Philbin, J. , Chum, O. , Isard, M. , Sivic, J. and Zisserman, A._ *Object retrieval with large vocabularies and fast spatial matching* - Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (2007) 
