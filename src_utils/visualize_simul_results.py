import json
from statistics import median
import matplotlib.pyplot as plt


FilenamePrioritizationProblem="../results/results/simul_res_MutantPrioritization.json"
FilenamesSetProblem=[f"../results/results/simul_res_MutantSetProblem_{p}percent.json" for p in [2,5,10]]

def viz_muPrioritizationProblem_res(simul_res_filename,Methods=['Random', 'Subsuming', 'FaultRevClf'],DisplayName=['Random', 'Subsuming', 'FaultRevClf'],BasedOn=['percentage_of_mu', 'percentage_of_tests'],lblY=["Percentage of mutants","Percentage of tests"],YLim=[-2,102],Facecolors = ['tab:red','tab:orange', 'tab:blue', 'tab:green']):
    with open(simul_res_filename,"r",encoding="UTF_8") as f:simul_res_dict = json.loads(f.read())
    for basedon,lY in zip(BasedOn,lblY):
        Viz_Data_Overall = []
        for method,displayName in zip(Methods,DisplayName):
            data_method = []
            for srcid in simul_res_dict[method]:#map_src_id_to_fault_complexity
                data_method += 100*simul_res_dict[method][str(srcid)][basedon]
            print(displayName,basedon, median(data_method))
            Viz_Data_Overall.append(data_method)
        fig, axs = plt.subplots(1)
        b = axs.boxplot(Viz_Data_Overall, patch_artist=True, medianprops={'color': 'black'})
        facecolors = Facecolors
        for box in b['boxes']:
            c = facecolors.pop(0)
            facecolors.append(c)
            box.set(facecolor=c)
        axs.set_ylim(YLim[0],YLim[1])
        axs.set_xticklabels(DisplayName)
        axs.set_ylabel(lY)
        axs.yaxis.grid(True)
        plt.tight_layout()
        plt.show()

def viz_muSetProblem_res(Filenames,Methods=['Random', 'Subsuming', 'FaultRev','Subsuming^FaultRev'],DisplayName=['Random', 'Subsuming', 'FaultRev','Subsuming^FaultRev'],BasedOn=['fault_rev_rate'],lblY=["Fault revealation rate"],YLim=[0.0,1.0],Percentage=[2,5,10,11],Facecolors = ['tab:red','tab:red','tab:orange', 'tab:purple','tab:blue', 'tab:green']):
    for basedon, lY in zip(BasedOn, lblY):
        Viz_Data_Overall = []
        x_ticks = []
        positions = []
        pos = 0
        for p,fname in zip(Percentage,Filenames):
            pos+=1
            with open(fname,"r",encoding="UTF_8") as f:simul_res_set_problem = json.loads(f.read())

            for method, displayName in zip(Methods, DisplayName):
                data_method = []
                for srcid in simul_res_set_problem[method].keys():
                    data_method += simul_res_set_problem[method][str(srcid)][basedon]
                print(displayName, basedon, median(data_method))
                Viz_Data_Overall.append(data_method)
                positions.append(pos)
                x_ticks.append(f"{displayName} {p}%")
                pos+=1

        fig, axs = plt.subplots(1)
        b = axs.boxplot(Viz_Data_Overall, positions=positions, patch_artist=True, medianprops={'color': 'black'})
        facecolors = Facecolors
        for box in b['boxes']:
            c = facecolors.pop(0)
            facecolors.append(c)
            box.set(facecolor=c)
        axs.set_ylim(YLim[0] - 0.02 , YLim[1] + 0.02)
        axs.set_xticklabels(x_ticks)
        axs.set_ylabel(lY)
        plt.margins(.05, .05)
        axs.tick_params(axis='x', rotation=90)
        axs.yaxis.grid(True)
        plt.tight_layout()
        plt.show()


viz_muPrioritizationProblem_res(FilenamePrioritizationProblem,Methods=['Random', 'Subsuming', 'FaultRev','Subsuming^FaultRev'],DisplayName=['Random', 'Subsuming', 'FaultRev','Subsuming^FaultRev'],BasedOn=['percentage_of_mu', 'percentage_of_tests'],lblY=["Percentage of mutants","Percentage of tests"],YLim=[-2,102])
viz_muSetProblem_res(Filenames=FilenamesSetProblem,Methods=['Random','Stmt_Del','E_Selective', 'Subsuming', 'FaultRev','Subsuming^FaultRev'],DisplayName=['Random','Stmt_Del','E_Selective', 'Subsuming', 'FaultRev','Subsuming^FaultRev'],Percentage=[2,5,10])

