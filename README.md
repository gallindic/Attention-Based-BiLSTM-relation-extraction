This is a forked project from `Attention-Based-BiLSTM-relation-extractio`(https://github.com/SeoSangwoo/Attention-Based-BiLSTM-relation-extraction).

## Datasets used
 - SemEval
 - TermFrame (EN/SL)

## Prerequisites

1. Run `pip install -r requirements.txt`
2. Run `python loader.py`

## Train

 Checkpoints will be generated in `run/[run_id]/checkpoints/`.

1. On SemEval
 - Run `python train.py --embedding_path "glove.6B.100d.txt" --num_epochs 40`.

2. On TermFrame (EN/SL)
 - Run `python train.py --train_path [path to train file] --test_path [path to test file] --embedding_path "glove.6B.100d.txt" --num_epochs 40 --mapped_labels 0`.

## Evaluation

1. On SemEval
- Run `python eval.py --checkpoint_dir "[eg. runs/1653211111/checkpoints/]"`.
- Run `python show_evaluation.py --predictions [eg. runs/1653211111/predictions.txt]`

2. On TermFrame (EN/SL)
- Run `python eval.py --checkpoint_dir "[eg. runs/1653211111/checkpoints/]" --test_path [path to test file used in training] --mapped_labels 0`
- Run `python show_evaluation.py --predictions [eg. runs/1653211111/predictions.txt] --test_path [path to test file used in training]`
- If checkpoint trained on SemEval is used, add `--mapped_labels 1`

## Transfer learning

1. Run `python train.py --embedding_path "glove.6B.100d.txt" --num_epochs 40 --mapped_labels 1` (Trained on SemEval).
2. Run `python train.py --checkpoint_dir "[from previous SemEval train] --train_path [path to train file (use mapped)] --test_path [path to test file (use mapped)] --embedding_path "glove.6B.100d.txt" --num_epochs 40 --mapped_labels 1 --transfer_learn 1`.
3. Run `python eval.py --checkpoint_dir "[from previous TermFrame train]" --test_path [path to test file used in training] --mapped_labels 1`
4. Run `python show_evaluation.py --predictions [eg. runs/1653211111/predictions.txt] --test_path [path to test file used in training]`