import argparse
from sklearn.metrics import f1_score

def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--test_path", default="SemEval2010_task8_all_data/SemEval2010_task8_testing_keys/TEST_FILE_FULL.TXT",
                        type=str, help="Path of test data")

    parser.add_argument("--predictions", required=1,
                        type=str, help="Path of predictions file")

    return parser.parse_args()


def main(args):
    gt = []
    correct = 0

    with open (args.test_path) as file:
        lines = file.readlines()

        for line in range(0, len(lines), 4):
            _, sentance = lines[line].split("\t")
            sentance = sentance.replace("\n", "")
            relation = lines[line + 1].replace("\n", "")

            gt.append((sentance, relation))

    with open (args.predictions) as file:
        pred = file.readlines()

    
    predictions = []
    real_gt = []

    for (predicted, real) in zip(pred, gt):
        predicted = predicted.split("\t")[1].strip()
        sentance, relation = real
        print(f'Sentace: {sentance}\nReal: {relation}\nPredicted: {predicted}\nCorrect: {predicted in relation}\n\n')
        
        if predicted == relation:
            correct += 1
        
        predictions.append(predicted)
        real_gt.append(relation)

        print(correct / len(gt))

    print(f'f1: {f1_score(predictions, real_gt, average="macro")}')
    print(f'accuracy: {correct, len(gt)}')


if __name__ == "__main__":
    args = parse_args()
    main(args)