import subprocess
import os
from multiprocessing import Pool

def Blast_Directory_Parallel(fasta_dir, blast_dir, nr_dir):
    p = Pool(4)
    args = [blast_dir, "-d", nr_dir, "-j", "3", "-b", "1", 
             "-a", "4", "-i", "test.fa", "-Q", "test.pssm"]
    all_args = []
    for file in os.listdir(fasta_dir):
        if ".fa" in file:
            fa_filename = fasta_dir + file
            pssm_filename = fasta_dir + file[:-6] + ".pssm"
            args[10] = fa_filename
            args[12] = pssm_filename
            all_args.append(args[:])
    p.map(_Blast_Directory, all_args)

def _Blast_Directory(args):
    print "Blasting: '{}' ...".format(args[12])
    FNULL = open(os.devnull, 'w')
    subprocess.call(args, stdout=FNULL)

def Extract_Features(pssm_dir):
    """
    Helper function for generating the dataset file
    :param sequences: list of proten sequences
    :return: return the extracted features from the sequences
    """
    for file in os.listdir(pssm_dir):
        if ".pssm" not in file:
            continue
        if os.path.exists(pssm_dir + file[:-5] + ".features"):
            continue
        feature_vectors = []
        pssm = Get_PSSM(pssm_dir + file)
        label_matrix = Get_Label_Matrix(pssm_dir + file[:-5] + ".rr")
        
        with open(pssm_dir + file[:-5] + ".features", "w") as feature_file:
            for label_key in label_matrix:
                i = label_key[0] + 2
                j = label_key[1] + 2
                d = label_key[2]
                i_features = pssm[i-2:i+3]
                j_features = pssm[j-2:j+3]
                i_flat = [item for sublist in i_features for item in sublist]
                j_flat = [item for sublist in j_features for item in sublist]
                i_str = ",".join(x for x in i_flat)
                j_str = ",".join(x for x in j_flat)
                feature_file.write("{},{},{}\n".format(d, i_str, j_str)) 

def Get_PSSM(blast_output):    
    pssm = []
    pssm.append(["-1" for _ in range(20)])
    pssm.append(["-1" for _ in range(20)])
    
    with open(blast_output, 'r') as pssm_file:
        start_read = False
        for line in pssm_file:
            if "Lambda" in line:
                break
            line = line.strip()
            if line == "":
                continue
            line = line.split()
            if line[0] == "1":
                start_read = True
            if start_read:
                scores = line[2:22]
                pssm.append(scores)
    
        pssm.append(["-1" for _ in range(20)])
        pssm.append(["-1" for _ in range(20)])
        
    return pssm

def Get_Label_Matrix(rr_filename):
    label_matrix = []
    with open(rr_filename, "r") as rr_file:
        start_read = False
        for line in rr_file:
            if not start_read:
                start_read = True
                continue
            line = line.strip().split(" ")
            i = int(line[0]) - 1
            j = int(line[1]) - 1
            d = line[4]
            label_matrix.append([i, j, line[4]])
    return label_matrix
        

if __name__ == "__main__":
    blast_dir = "../../blast/bin/blastpgp"
    nr_dir = "../../nr/nr"
    #Blast_Directory_Parallel("data/", blast_dir, nr_dir)
    Extract_Features("data/")        
