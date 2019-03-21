#!/usr/bin/env python3

import re
import itertools

ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
    

    def make_ageasensi_list(self):
        '''
        Makes an adjacency list of all the the vertices 
        Returns:
        A nested list where index of each element represent the node and the list 
        corrosponding to that index is the adjacency list of that inde        
        '''
        vertices=self.vertices[:]
        lines=self.edges[:]

        final_list=[]
        '''
        It is of the form of Adjacency List
        '''
        for j in vertices:
            list_to_append_in_final_list=[]
            for i in lines:         # This part if code checks all the vetics connected to corrosponding vertics then  append them in a list and then finally append the hole thing to fianl list

                if (i[0]==j):
                    list_to_append_in_final_list.append(i[1])

                elif (i[1]==j) :
                    list_to_append_in_final_list.append(i[0])

            final_list.append([list_to_append_in_final_list])

        return final_list        






    def extract_x_and_y_from_all_path(self,all_path,node) :


        '''This function returns X and Y from the all the shortest path  
		Args:
			allpath- list of all the shortest path
			node- Node for which we are checking the betweenness centrality 
        
		Returns-
        	No. of shortest path between the node pair (X)

        	No. of shortest path between the node pair passing through Node (Y)
        '''

        #Initialisation
        total_number_of_path=1
        multiple_level_part_in_path=[]
        single_level_part_in_path=[]
        no_of_path_having_node=0


        for i in all_path :

            
            if (isinstance(i,list) ):
                total_number_of_path=total_number_of_path*len(i)
                multiple_level_part_in_path.append(i)
            else :
                single_level_part_in_path.append(i)


        if(node in single_level_part_in_path):
            return [total_number_of_path,total_number_of_path]
        else :
            for i in multiple_level_part_in_path :
                if (node in i ):
                    temp=total_number_of_path/len(i)
                    no_of_path_having_node=temp*(len(i)-1)
                    return [total_number_of_path,no_of_path_having_node]
        return [total_number_of_path,0]    



    def all_paths(self,start_node, end_node):
        """
        Finds all shortest paths from node to destination 

        Args:
            node: Node to find path from
            start_node:Starting node 
            end_node: Ending Node
            

        Returns:
            List of path, where each path is list ending on destination

            
        """

        #origin_table(precidance table) tells from where the node is created 
        #flag_table tell whether number is checked or not
       
        vertices=self.vertices[:]
        lines=self.edges[:]

        #This is a bfs implimentation

        origin_table=[]
        flag_table=[]
        distance=[]
        adjacency_list=self.make_ageasensi_list()
         #Initialisation
        for i in vertices :
            origin_table.append([])
            flag_table.append(False)
            distance.append(50000)
        path=[]
        queue=[]
        flag_table[start_node-1]=True
        distance[start_node-1]=0


        queue.append(start_node)

        while len(queue)!=0 :
            current_node_which_we_are_checking=queue[0]
            queue=queue[1:]
            for i in adjacency_list[current_node_which_we_are_checking-1] :
                
                for current_neighbour in i :
                    if flag_table[current_neighbour-1]==False :
                        flag_table[current_neighbour-1]=True
                        
                        distance[current_neighbour-1]=distance[current_node_which_we_are_checking-1]+1
                        queue.append(current_neighbour)

                    if  distance[current_neighbour-1]==distance[current_node_which_we_are_checking-1]+1 :
                        origin_table[current_neighbour-1].append(current_node_which_we_are_checking)


        #bfs implimentation ends here 

        #This part of the code backtraces the steps to find all the steps involved
        #This previous v is used to ensure that it prints all the elements of the level if there are two or more path 

        currentV = end_node
        previous_v=-5
        
        final_steps_to_reach_from_start_to_end=[]
        
        while (len(origin_table[currentV-1]) != 0) :
            if(previous_v!= -5):
                final_steps_to_reach_from_start_to_end.append(previous_v)
                previous_v=-5
            else :
                final_steps_to_reach_from_start_to_end.append(currentV)        
            if (len(origin_table[currentV-1])>1):
                previous_v=origin_table[currentV-1]
                
            currentV = origin_table[currentV-1][0]

        final_steps_to_reach_from_start_to_end.append(start_node)

            

        return final_steps_to_reach_from_start_to_end

        raise NotImplementedError

    def betweenness_centrality(self, node):
        """
        Find betweenness centrality of the given node

        Args:
            node: Node to find betweenness centrality of.

        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        """

        vertices=self.vertices[:]
        lines=self.edges[:]
        original=list(vertices)
        betweenness_centrality_of_node=0                 #To remove the node we are checking

        i=1
        if(i==node):    #To confirm the node is not passed as the starting or ending node
            i=i+1
        while (i<=len(vertices)) :
            j=1
            j=i+1
            if(j==node):    #To confirm the node is not passed as the starting or ending node
            	j=j+1

            while (j<=len(vertices)) :
                
                
                #To be changed when finalised
                all_paths=self.all_paths(i,j)
                
                data_from_the_function=self.extract_x_and_y_from_all_path(all_paths,node)
                
                no_of_shortest_path=data_from_the_function[0]

                no_of_path_passing_through_node=data_from_the_function[1]

                betweenness_centrality_of_node=betweenness_centrality_of_node+no_of_path_passing_through_node/no_of_shortest_path

                if(j+1==node):    #To confirm the node is not passed as the starting or ending node
                    j=j+1
                j+=1

            if(i+1==node):          #To confirm the node is not passed as the starting or ending node
                i=i+1
            i+=1


        
        return(betweenness_centrality_of_node)



        raise NotImplementedError

    def top_k_betweenness_centrality(self):
        """
        Find top k nodes based on highest equal betweenness centrality.

        
        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """
        vertices=self.vertices[:]
        lines=self.edges[:]

        centrality=[]
        index=0
        biggest=0

        #To find the biggest value of betweeness centrality
        for i in vertices :
        	
        	a=self.betweenness_centrality(i)
        	centrality.append(a)
        	if a>biggest:
        		biggest=a
        # To find the index corrosponding to it 
        ans=[]
        index=0     
        for i in centrality :
            index+=1
            if i == biggest :
                ans.append(index)

                    
        return ans

        raise NotImplementedError





if __name__ == "__main__":

    #Please start the values of vertices from 1 
    vertices = [1, 2, 3, 4,5,6,7,8]


    edges  = [(1,2), (1, 3), (2, 3), (3, 4), (2, 6), (3,5), (4, 5), (4,6), (5,6), (6,8), (6,7), (5,8), (7,8), (5,7)]

    graph = Graph(vertices, edges)

    print(graph.top_k_betweenness_centrality())
