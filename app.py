from itertools import count
from numpy import zeros
from soupsieve import select
import streamlit as st



def main():
    select_count = 4
    bay_count = 0
    freq_count = 0
    st.title("Are you a Bayesian or Frequentist at heart?")
    st.text("Provide answers to these following scenarios to be revealed your statistical identity.")
    q_one_options = ["Select","I prefer set rules", "I prefer to go based on intuition"]
    q_one = st.selectbox("Do you prefer having set rules to follow when running a project/experiment/analysis or do you like to make decisions off of intuition?", q_one_options, index=0)
    zero_percent = 0.0
    hundred_percent = 1.0
    fifty_percent = 0.5
    q_two_options = ["Select", "The probability that it is heads is either {:.0%} or {:.0%}, no doubt".format(zero_percent, hundred_percent), "The probability that it is heads is {:.0%} ".format(fifty_percent)]
    q_two = st.selectbox("If I tossed a coin in my hand and it has already landed but you don't know if it is heads or tails, what is the probability that it is heads?", q_two_options)
    q_three_options = ["Select", "I would not use previous data because it could be outdated/completely different location which wont provide any useful information for the current sailor lost.", "I would use previous data of where other sailors got lost at sea because it could reveal patterns or niche information of where the lost sailor could be."]
    q_three = st.selectbox("If a sailor was lost at sea and you were in charge of trying to find the sailor, would you use previous data of where other sailors have gotten lost at sea or just the inforamtion you know so far of the sailor (ex. beginning and end destination)?", q_three_options)
    q_four_options = ["Select", "I consider my previous views to be wrong and current views to be right", "I consider my previous and current views to be neither right or wrong, but just changing as new information is given to me"]
    q_four = st.selectbox("When you change your viewpoint on something, do you believe that your current view was right and the previous view was wrong OR do you believe that the previous and current view isn't necessarily right or wrong but changes over time as new data/information is given to you.", q_four_options)



    if q_one == q_one_options[1]:
        freq_count += 1
        select_count -= 1
    elif q_one == q_one_options[2]:
        bay_count += 1
        select_count -= 1
    if q_two == q_two_options[1]:
        freq_count += 1
        select_count -= 1
    elif q_two == q_two_options[2]:
        bay_count += 1
        select_count -= 1
    if q_three == q_three_options[1]:
        freq_count += 1
        select_count -= 1
    elif q_three == q_three_options[2]:
        bay_count += 1
        select_count -= 1
    if q_four == q_four_options[1]:
        freq_count += 1
        select_count -= 1
    elif q_four == q_four_options[2]:
        bay_count += 1
        select_count -= 1
    
    if select_count == 0:
        if bay_count > freq_count:
            st.header("You are a Bayesian at heart!")
            st.text("You like to make decisions based on intuition and you would be likely to use statistics to update your prior beliefs.")
            st.text("Remember that Bayesian methods may not work for all situations and it's fair to be aware that both idealogies play an important role in different types of situations depending on the problem at hand.")
        elif bay_count < freq_count:
            st.header("You are a Frequentist at heart!")
            st.text("You like to make decisions based on the data at hand and you would be likely to use statistics to find a right/wrong or to decide what action to take. You also like when there are firm rules to follow.")
            st.text("Remember that Bayesian methods may not work for all situations and it's fair to be aware that both idealogies play an important role in different types of situations depending on the problem at hand.")
        elif bay_count == freq_count:
            st.header("You are a neither!")
            st.text("You are inbetween being strictly a Bayesian or Frequentist. You probably think these different methods come into play differently depending on the situation. Sometimes you think there should be firm rules and other times you think intuition would work better.")
    
    #st.text("Bayesian: {}, Frequentist: {}".format(bay_count, freq_count))

if __name__ == '__main__':
    main()