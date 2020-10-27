all:
	make scatter
	make csv
	
requirements.txt: FORCE
	pip freeze >| requirements.txt

FORCE:

scatter: 
	make task1/output/1d2d_desc_LinearRegression_train.png
	make task1/output/1d2d_desc_LinearRegression_test.png
	make task1/output/1d2d_desc_Ridge_train.png
	make task1/output/1d2d_desc_Ridge_test.png
	make task1/output/1d2d_desc_SVR_train.png
	make task1/output/1d2d_desc_SVR_test.png
	make task1/output/1d2d_desc_RandomForest_train.png
	make task1/output/1d2d_desc_RandomForest_test.png
	make task1/output/1d2d_desc_LightGBM_train.png
	make task1/output/1d2d_desc_LightGBM_test.png
	#
	make task1/output/3d_desc_LinearRegression_train.png
	make task1/output/3d_desc_LinearRegression_test.png
	make task1/output/3d_desc_Ridge_train.png
	make task1/output/3d_desc_Ridge_test.png
	make task1/output/3d_desc_SVR_train.png
	make task1/output/3d_desc_SVR_test.png
	make task1/output/3d_desc_RandomForest_train.png
	make task1/output/3d_desc_RandomForest_test.png
	make task1/output/3d_desc_LightGBM_train.png
	make task1/output/3d_desc_LightGBM_test.png
	#
	make task1/output/fp_LinearRegression_train.png
	make task1/output/fp_LinearRegression_test.png
	make task1/output/fp_Ridge_train.png
	make task1/output/fp_Ridge_test.png
	make task1/output/fp_SVR_train.png
	make task1/output/fp_SVR_test.png
	make task1/output/fp_RandomForest_train.png
	make task1/output/fp_RandomForest_test.png
	make task1/output/fp_LightGBM_train.png
	make task1/output/fp_LightGBM_test.png
	#
	#
	make task2/output/1d2d_desc_LinearRegression_train.png
	make task2/output/1d2d_desc_LinearRegression_test.png
	make task2/output/1d2d_desc_Ridge_train.png
	make task2/output/1d2d_desc_Ridge_test.png
	make task2/output/1d2d_desc_SVR_train.png
	make task2/output/1d2d_desc_SVR_test.png
	make task2/output/1d2d_desc_RandomForest_train.png
	make task2/output/1d2d_desc_RandomForest_test.png
	make task2/output/1d2d_desc_LightGBM_train.png
	make task2/output/1d2d_desc_LightGBM_test.png
	#
	make task2/output/3d_desc_LinearRegression_train.png
	make task2/output/3d_desc_LinearRegression_test.png
	make task2/output/3d_desc_Ridge_train.png
	make task2/output/3d_desc_Ridge_test.png
	make task2/output/3d_desc_SVR_train.png
	make task2/output/3d_desc_SVR_test.png
	make task2/output/3d_desc_RandomForest_train.png
	make task2/output/3d_desc_RandomForest_test.png
	make task2/output/3d_desc_LightGBM_train.png
	make task2/output/3d_desc_LightGBM_test.png
	#
	make task2/output/fp_LinearRegression_train.png
	make task2/output/fp_LinearRegression_test.png
	make task2/output/fp_Ridge_train.png
	make task2/output/fp_Ridge_test.png
	make task2/output/fp_SVR_train.png
	make task2/output/fp_SVR_test.png
	make task2/output/fp_RandomForest_train.png
	make task2/output/fp_RandomForest_test.png
	make task2/output/fp_LightGBM_train.png
	make task2/output/fp_LightGBM_test.png

csv:
	make task1/output/rmse_q2.csv
	make task1/output/rmse_q2_diff.csv
	make task2/output/rmse_q2.csv
	make task2/output/rmse_q2_diff.csv

task1/output/%.png: task1/output/%.csv task1/csv_to_scatter.py
	python ./task1/csv_to_scatter.py $<

task1/output/rmse_q2.csv: task1/rmse_q2_list.py
	python ./task1/rmse_q2_list.py

task1/output/rmse_q2_diff.csv: task1/rmse_q2_list.py
	python ./task1/rmse_q2_list.py

task2/output/%.png: task2/output/%.csv task2/csv_to_scatter.py
	python ./task2/csv_to_scatter.py $<

task2/output/rmse_q2.csv: task2/rmse_q2_list.py
	python ./task2/rmse_q2_list.py

task2/output/rmse_q2_diff.csv: task2/rmse_q2_list.py
	python ./task2/rmse_q2_list.py

clean:
	rm -rf ./task1/output/*.png
	rm -rf ./task1/output/rmse_q2.csv ./task2/output/rmse_q2_diff.csv
	rm -rf ./task2/output/*.png
	rm -rf ./task2/output/rmse_q2.csv ./task2/output/rmse_q2_diff.csv

