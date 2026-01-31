import librosa
import numpy as np

AI_file = "/media/alchemax/New Volume/Programming_Files/python_GIT/Librosa_concept/sample_voice.mp3"
Human_file = "/media/alchemax/New Volume/Programming_Files/python_GIT/Librosa_concept/my_voice2.mp3"


def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)

    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    zcr = librosa.feature.zero_crossing_rate(y)
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)

    f0, voiced_flag, _ = librosa.pyin(y, fmin=50, fmax=300, sr=sr)
    pitch = f0[voiced_flag]

    return {
        "mfcc": mfccs,
        "zcr": zcr,
        "centroid": centroid,
        "rms": rms,
        "pitch": pitch
    }


def compute_stat(feature, stat):
    if stat == "mean":
        return np.mean(feature)
    elif stat == "std":
        return np.std(feature)
    elif stat == "var":
        return np.var(feature)
    elif stat == "mean_diff":
        return np.mean(np.diff(feature))
    else:
        raise ValueError("Invalid stat")


# Load features
ai_features = extract_features(AI_file)
human_features = extract_features(Human_file)

# ---- MENU SYSTEM ----
while True:
    print("\nChoose Statistic:")
    print("1. mean")
    print("2. std")
    print("3. var")
    print("4. mean_diff")
    print("5. exit")

    stat_choice = input("Enter choice: ")

    stat_map = {
        "1": "mean",
        "2": "std",
        "3": "var",
        "4": "mean_diff"
    }

    if stat_choice == "5":
        print("Exiting...")
        break

    stat = stat_map.get(stat_choice)
    if stat is None:
        print("Invalid choice")
        continue

    print("\nChoose Feature:")
    print("1. mfcc")
    print("2. zcr")
    print("3. centroid")
    print("4. rms")
    print("5. pitch")

    feat_choice = input("Enter choice: ")

    feat_map = {
        "1": "mfcc",
        "2": "zcr",
        "3": "centroid",
        "4": "rms",
        "5": "pitch"
    }

    feature = feat_map.get(feat_choice)
    if feature is None:
        print("Invalid choice")
        continue

    ai_value = compute_stat(ai_features[feature], stat)
    human_value = compute_stat(human_features[feature], stat)

    print(f"\n📊 Comparison ({stat.upper()} of {feature.upper()})")
    print(f"AI Voice    : {ai_value:.4f}")
    print(f"Human Voice : {human_value:.4f}")
