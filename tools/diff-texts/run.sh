INPUT_FOLDER=$CROSSCOMPUTE_INPUT_FOLDER
OUTPUT_FOLDER=$CROSSCOMPUTE_OUTPUT_FOLDER
diff -ty $INPUT_FOLDER/text1.txt $INPUT_FOLDER/text2.txt > $OUTPUT_FOLDER/diff.txt